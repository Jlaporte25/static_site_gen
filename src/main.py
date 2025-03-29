import htmlnode
from block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
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
        children = []
        for block in blocks:
            if not block.strip():
                continue

            bl_type = block_to_block_type(block)
            if bl_type == BlockType.CODE:
                htmln = [
                    TextNode(block.strip(), TextType.CODE)
                ]  # No inline parsing for CODE blocks
            else:
                tnodes = text_to_textnodes(block)
                htmln = [text_node_to_html_node(node) for node in tnodes]

            if bl_type == BlockType.PARAGRAPH:
                children.append(HTMLNode("p", htmln, None))
            elif bl_type == BlockType.HEADING:
                heading_level = block.count("#", 0, block.find(" "))
                stripped_block = block.lstrip("#").strip()
                tag = f"h{heading_level}"
                children.append(HTMLNode(tag, htmln, None))
            elif bl_type == BlockType.UNORDERED_LIST:
                list_items = [
                    HTMLNode(
                        "li", [text_node_to_html_node(item.lstrip("-").strip())], None
                    )
                    for item in block.split_nodes_delimiter("-")
                    if item.strip()
                ]
                children.append(HTMLNode("ul", list_items, None))
            elif bl_type == BlockType.ORDERED_LIST:
                list_items = [
                    HTMLNode(
                        "li",
                        [text_node_to_html_node(item.split(maxsplit=1)[-1].strip())],
                        None,
                    )
                    for item in block.split("\n")
                    if item.strip()
                ]
                children.append(HTMLNode("ol", list_items, None))
            elif bl_type == BlockType.QUOTE:
                children.append(HTMLNode("blockquote", htmln, None))
            elif bl_type == BlockType.CODE:
                code_inner = HTMLNode(
                    "code", [TextNode(block.strip(), TextType.CODE)], None
                )
                children.append(HTMLNode("pre", [code_inner], None))
            else:
                raise ValueError(f"Unhandled block type: {bl_type}")
        parent_node = ParentNode("div", children, None)
        return parent_node

    md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """
    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)


if __name__ == "__main__":
    main()
