from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from split_node import split_nodes_delimiter
from text_to_html import text_node_to_html_node


def main():

    node = TextNode("This is **text** with a **bold** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)


if __name__ == "__main__":
    main()
