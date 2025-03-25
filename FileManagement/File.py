
from Entry import Entry
from Tag import Tag

class File(Entry):

    def __init__(self, name, content):
        super().__init__(name)
        self.content = content
        self.tags = []

    def updateContent(self, newContent):
        self.content = newContent

    def toJSON():
        pass
