from enum import Enum


class TextNode(Enum):
    def __init__(text, text_type, url):
        super().__init__(TextType)
        self.text = text
        self.text_type = text_type
        self.url = url

    def __repr__(self):
        return f"{self}({self.text}, {self.text_type.value()}, {self.url})"
