import htmlnode
from block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from split_node import (split_nodes_delimiter, split_nodes_image,
                        split_nodes_link)
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType


def main():
    def text_to_textnodes(text):
        node = TextNode(text, TextType.TEXT)
        split_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
        split_italic = split_nodes_delimiter(split_bold, "_", TextType.ITALIC)
        split_code = split_nodes_delimiter(split_italic, "`", TextType.CODE)
        split_images = split_nodes_image(split_code)
        split_final = split_nodes_link(split_images)
        return split_final

    def markdown_to_html_node(markdown):
        blocks = markdown_to_blocks(markdown)
        for block in blocks:
            bl_type = block_to_block_type(block)
            children = text_to_children(block)

    def text_to_children(text):
        text_nodes = text_to_textnodes(text)
        return text_nodes

    md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """
    print(markdown_to_html_node(md))


if __name__ == "__main__":
    main()
