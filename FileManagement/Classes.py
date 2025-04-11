
class Tag:
    def __init__(self, name: str, color: str = "default"):
        self.name = name
        self.color = color

    def __eq__(self, other):
        # check if two Tags are equal based on name
        if isinstance(other, Tag):
            return self.name == other.name
        return False

    def __repr__(self):
        # return a string representation of Tag
        return f"Tag(name={self.name}, color={self.color})"


class Entry:
    def __init__(self, id, parentId, name, createdAt):
        self.id = id
        self.parentId = parentId
        self.name = name
        self.createdAt = createdAt

    def getId(self):
        return self.id
    
    def getParentId(self):
        return self.parentId

    def getName(self):
        return self.name

    def getCreatedAt(self):
        return self.createdAt


class Folder(Entry):
    def __init__(self, id, parentId, name, createdAt):
        super().__init__(id, parentId, name, createdAt)


class File(Entry):
    def __init__(self, id, parentId, name, createdAt, tags):
        super().__init__(id, parentId, name, createdAt)
        self.tags = tags

    def getTags(self):
        return self.tags
    
    def addTag(self, tag: Tag):
        self.tags.append(tag)

    def removeTag(self, tag: Tag):
        if (tag in self.tags):
            self.tags.remove(tag)

