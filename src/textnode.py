from enum import Enum

import re

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url)
    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type.value}, "{self.url}")'

def text_node_to_html_node(text_node):
    type = text_node.text_type
    text = text_node.text
    if type == TextType.TEXT:
        return LeafNode(None, text)
    elif type == TextType.BOLD:
        return LeafNode("b", text)
    elif type == TextType.ITALIC:
        return LeafNode('i', text)
    elif type == TextType.CODE:
        return LeafNode("code", text)
    elif type == TextType.LINK:
        return LeafNode("a", text, {"href": text_node.url})
    elif type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text})
    else:
        raise Exception("Invalid TextType")





