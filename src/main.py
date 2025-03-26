from htmlnode import HTMLNode, LeafNode, ParentNode
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

    def markdown_to_blocks(markdown):
        split_mark = markdown.split("\n\n")
        new_list = []
        for mark in split_mark:
            if len(mark) > 0:
                stripped = mark.strip()
                final = stripped.strip(" ")
                new_list.append(final)

        return new_list

    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """

    print(markdown_to_blocks(md))


if __name__ == "__main__":
    main()
