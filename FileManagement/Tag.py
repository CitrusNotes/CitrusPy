
class Tag:

    def __init__(self, name: str, color: str = "default"):
        # initialize a Tag with a name and optional color
        self.name = name
        self.color = color

    def __eq__(self, other):
        # check if two Tags are equal based on name
        if isinstance(other, Tag):
            return self.name == other.name
        return False

    def __repr__(self) -> str:
        # return a string representation of Tag
        return f"Tag(name={self.name}, color={self.color})"












