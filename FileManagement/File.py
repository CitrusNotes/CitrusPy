'''
- name
- path
- size
- date_created
- date_modified
- owner
- permissions
- is_trash
- is_starred
- more ?
'''

from Tag import Tag

class File:

    def __init__(self, name, content):
        self.name = name
        self.path = None # path will be set later?
        self.tags = []
        self.is_starred = False
        self.content = content
        self.created_at = None # handle content metadata later
        self.modified_at = None # handle content metadata later
        self.size = None # handle content metadata later

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

