from block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
import htmlnode
from markdown_to_blocks import markdown_to_blocks
from textnode import TextNode, TextType
from split_node import split_nodes_delimiter, split_nodes_link, split_nodes_image
from text_to_html import text_node_to_html_node


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

    def text_to_children(text):
        pass

    md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """
    print(markdown_to_html_node(md))


if __name__ == "__main__":
    main()
