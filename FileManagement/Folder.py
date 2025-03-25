
from File import File
from Tag import Tag

class Folder:

    def __init__(self, name):
        self.name = name
        self.path = None
        self.files = []
        self.subfolders = []
        self.tags = []
        self.is_starred = False
        self.created_at = None # handle content metadata later
        self.modified_at = None # handle content metadata later
        self.size = None # handle content metadata later

    def getName(self):
        return self.name
    
    def getPath(self):
        return self.path
    
    def getSize(self):
        return self.size
    
    def addFile(self, file):
        # to be implemented
        pass

    def removeFile(self, file):
        # to be implemented
        pass

    def addSubfolder(self, folder):
        # to be implemented
        pass

    def removeSubfolder(self, folder):
        # to be implemented
        pass

