from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType


def main():
    html_node = LeafNode(
        "a",
        "Click Me",
        {"href": "https://www.google.com", "target": "_blank"},
    )
    print(html_node.to_html())


if __name__ == "__main__":
    main()
