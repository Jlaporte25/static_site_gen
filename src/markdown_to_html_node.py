from block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_to_html import text_node_to_html_node
from textnode import TextNode
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        if not block.strip():
            continue

        bl_type = block_to_block_type(block)
        tnodes = text_to_textnodes(block)
        htmln = [text_node_to_html_node(node) for node in tnodes]
        if bl_type == BlockType.PARAGRAPH:
            children.append(HTMLNode("p", htmln, None))
        elif bl_type == BlockType.HEADING:
            stripped_block = block.lstrip("#").strip()
            heading_level = stripped_block.count("#", 0, block.find(" "))
            tag = f"h{heading_level}"
            children.append(HTMLNode(tag, htmln, None))
        elif bl_type == BlockType.UNORDERED_LIST:
            list_items = [
                HTMLNode("li", [text_node_to_html_node(item.lstrip("-").strip())], None)
                for item in block.split("\n")
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
            code_inner = HTMLNode("code", [TextNode(block.strip())], None)
            children.append(HTMLNode("pre", [code_inner], None))
        else:
            raise ValueError(f"Unhandled block type: {bl_type}")
    parent_node = ParentNode("div", children, None)
    return parent_node
