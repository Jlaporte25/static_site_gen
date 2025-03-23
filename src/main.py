from typing import Text
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def main():
    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(None, self.value, None)
        elif self.text_type == TextType.BOLD:
            return LeafNode("b", self.value, None)
        elif self.text_type == TextType.ITALIC:
            return LeafNode("i", self.value, None)
        elif self.text_type == TextType.CODE:
            return LeafNode("code", self.value, None)
        elif self.text_type == TextType.LINK:
            return LeafNode("a", self.value, {"href": f"{self.url}"})
        elif self.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": f"{self.url}", "alt": f"{self.value}"})
        else:
            raise Exception

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())


if __name__ == "__main__":
    main()
