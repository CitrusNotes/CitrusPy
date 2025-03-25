
from Entry import Entry
from File import File
from Tag import Tag

class Folder(Entry):

    def __init__(self, name):
        super().__init__(name)
        self.files = []
        self.subfolders = []
    
    def addFile(self, file):
        if not isinstance(file, File):
            raise TypeError("file must be an instance of File class")
        if file not in self.files:
            self.files.append(file)

    def removeFile(self, file):
        if not isinstance(file, File):
            raise TypeError("file must be an instance of File class")
        if file in self.files:
            self.files.remove(file)

    def addSubfolder(self, folder):
        if not isinstance(folder, Folder):
            raise TypeError("folder must be an instance of Folder class")
        if folder not in self.subfolders:
            self.subfolders.append(folder)

    def removeSubfolder(self, folder):
        if not isinstance(folder, Folder):
            raise TypeError("folder must be an instance of Folder class")
        if folder in self.subfolders:
            self.subfolders.remove(folder)

    def toJSON():
        pass
