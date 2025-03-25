
from Tag import Tag

class Entry:

    def __init__(self, name, tags=None):
        self.name = name
        self.path = None # handle later
        self.size = None # handle later
        self.created_at = None # handle later
        self.modified_at = None # handle later
        self.is_starred = False
        self.tags = tags if tags is not None else []

    def getName(self):
        return self.name
    
    def getPath(self):
        return self.path

    def getSize(self):
        return self.size
    
    def getStarred(self):
        return self.is_starred
    
    def setStarred(self, starred):
        self.is_starred = starred

    def getTags(self):
        return self.tags

    def addTag(self, tag):
        # handle exception later
        if not isinstance(tag, Tag):
            raise TypeError("tag must be an instance of Tag class")
        
        if tag not in self.tags:
            self.tags.append(tag)
        
    def removeTag(self, tag):
        # handle exception later
        if not isinstance(tag, Tag):
            raise TypeError("tag must be an instance of Tag class")
        
        if tag in self.tags:
            self.tags.remove(tag)

    def toJSON():
        pass


