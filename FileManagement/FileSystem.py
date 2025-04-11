# main.py
from fastapi import FastAPI, HTTPException, UploadFile, File as UploadFileparam, Depends, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import datetime
from typing import List, Union, Optional
import uvicorn
import os

from Classes import Tag, Entry, Folder, File

app = FastAPI()

# pydantic response models for standardizing returned json data
# probably should put in another file, Models.py
class TagResponse(BaseModel):
    name: str
    color: str

class FileChildResponse(BaseModel):
    type: str = "file"
    name: str
    download_url: str
    tags: List[TagResponse]

class FolderChildResponse(BaseModel):
    type: str = "folder"
    name: str
    view_url: str

class FolderViewResponse(BaseModel):
    name: str
    path: str
    date_created: datetime
    children: List[Union[FileChildResponse, FolderChildResponse]]

# database should use an adjacency list model for managing the filesystem tree (no circular dependencies)
# using global ids and parent ids to ensure uniqueness of entries. the real database should implement 
# something similar.
# globalId, parentId, name, datecreated, (tags for files)
fakeDb = {
    1: Folder(1, 2, "test", datetime(2025, 4, 11)),
    2: Folder(2, 0, "carrot", datetime(2025, 4, 12)),
    3: File(3, 1, "test_file.txt", datetime(2025, 1, 1), [Tag("tag1", "blue"), Tag("tag2", "green")]),
    4: File(4, 1, "another_file.txt", datetime(2025, 2, 2), [Tag("asfkjldjklasl kgdh  cjkxnbvbvxc")]),
    5: Folder(5, 0, "orange", datetime(2025, 4, 13)),
    6: Folder(6, 0, "apple", datetime(2025, 4, 14))
}

# sort this out later
fakeTags = {
    1: Tag("tag1", "blue"),
    2: Tag("tag2", "green"),
    3: Tag("asfkjldjklasl kgdh  cjkxnbvbvxc")
}

# helper functions for the backend to compute stuff before sending to frontend
# also should put in another file, utils.py, once this gets large enough
def getPath(entry: Entry):
    path = "/"
    current = entry
    while (current.getParentId() != 0):
        path = "/" + current.getName() + path
        current = fakeDb.get(current.getParentId())
    return path

def getFolderChildren(folder: Folder):
    children = []
    for entry in fakeDb.values():
        if entry.getParentId() == folder.getId():
            children.append(entry)
    return children
    
def getTagResponses(tags: List[Tag]):
    return [TagResponse(name=t.name, color=t.color) for t in tags]

# view folder endpoint
@app.get("/folder/{folderId}")
def get_folder_content(folderId: int):
    # right now, we simulate database queries with the fakeDb. replace later once real db is sorted out
    # query database for folder with id folder_id, make sure it exists
    folder = fakeDb.get(folderId)
    if folder is None:
        raise HTTPException(status_code=404, detail="Folder not found")
    if not isinstance(folder, Folder):
        raise HTTPException(status_code=404, detail="Cannot view non folder id")
    
    # query database for all entries with parent node = to folderId, store in children
    child_responses = []
    children = getFolderChildren(folder)
    for child in children:
        if isinstance(child, Folder):
            child_responses.append(FolderChildResponse(
                name=child.getName(),
                view_url=f"/folder/{child.id}"
            ))
        elif isinstance(child, File):
            child_responses.append(FileChildResponse(
                name=child.getName(),
                download_url=f"/file/download/{child.id}",
                tags = getTagResponses(child.getTags())
            ))
    
    return FolderViewResponse(
        name = folder.getName(),
        path = getPath(folder),
        date_created = folder.getCreatedAt(),
        children = child_responses
    )



# possibly make a view file endpoint, for viewing file properties? wouldn't be too hard



class FolderCreateRequest(BaseModel):
    parentId: int
    name: str
    createdAt: datetime

# create folder endpoint
@app.post("/folder")
def create_folder(folderReq: FolderCreateRequest):
    # replace this new id generation with some database global id updating
    newId = max(fakeDb.keys(), default=0) + 1
    # again, replace this global id checking with the actual database query
    if folderReq.parentId != 0 and folderReq.parentId not in fakeDb:
        raise HTTPException(status_code=404, detail="Parent folder not found")
    
    newFolder = Folder(newId, folderReq.parentId, folderReq.name, folderReq.createdAt)
    fakeDb[newId] = newFolder

    return {"message": "Folder created successfully", "id": newId}


class FileCreateRequest(BaseModel):
    parentId: int
    name: str
    createdAt: datetime
    tags: Optional[List[int]] = []

    @classmethod
    def as_form(
        cls,
        parentId: int = Form(...),
        name: str = Form(...),
        createdAt: datetime = Form(...),
        tags: Optional[List[int]] = Form(None)
    ):
        if tags is None:
            tags = []
        return cls(parentId=parentId, name=name, createdAt=createdAt, tags=tags)

# create file endpoint
@app.post("/file")
async def create_file(
    metadata: FileCreateRequest = Depends(FileCreateRequest.as_form),
    fileData: UploadFile = UploadFileparam(...)
):
    # replace everything with database queries
    newId = max(fakeDb.keys(), default=0) + 1
    if metadata.parentId != 0 and metadata.parentId not in fakeDb:
        raise HTTPException(status_code=404, detail="Parent folder not found")
    
    uploads_dir = "uploads"
    os.makedirs(uploads_dir, exist_ok=True)
    file_location = os.path.join(uploads_dir, fileData.filename)
    try:
        with open(file_location, "wb") as f:
            content = await fileData.read()
            f.write(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")

    # handle creating tags later, once we discuss how to manage them
    tags = []

    newFile = File(newId, metadata.parentId, metadata.name, metadata.createdAt, tags)
    fakeDb[newId] = newFile
    
    return {"message": "File created successfully", "id": newId}


# delete folder endpoint (requires some recursion to make sure all subentries are deleted too)
@app.delete("/folder/{folderId}")
def delete_folder(folderId: int):
    return {"message": "not implemented yet"}


# delete entry endpoint
@app.delete("/file/{fileId}")
def delete_file(fileId: int):
    file = fakeDb.get(fileId)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    if not isinstance(file, File):
        raise HTTPException(status_code=400, detail="Specified entry is not a file")

    del fakeDb[fileId]
    return {"message": "File deleted successfully", "id": fileId}


# download file endpoint
@app.get("/file/download/{file_id}")
def download_file(fileId: int):
    file = fakeDb.get(fileId)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    if not isinstance(file, File):
        raise HTTPException(status_code=400, detail="Specified entry is not a file")
    
    # assume files are stored as "uploads/<filename>" for now. database later
    uploads_dir = "uploads"
    file_path = os.path.join(uploads_dir, file.getName())
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File content not found")
    
    return FileResponse(path=file_path, media_type="application/octet-stream", filename=file.getName())



if __name__ == "__main__":
    # run with: uvicorn FileSystem:app --reload
    uvicorn.run("FileSystem:app", host="127.0.0.1", port=8000, reload=True)


