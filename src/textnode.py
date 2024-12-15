from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other_node): # returns true if another TextNode has identical properties
        if self.text == other_node.text and self.text_type == other_node.text_type and self.url == other_node.url:
            return True
    
    def __repr__(self): # returns the textnode and its properties as a string like you'd see it in code, e.g. TextNode(x, y, z)
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"