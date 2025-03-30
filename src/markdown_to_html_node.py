from block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        if not block.strip():
            continue

        block_type = block_to_block_type(block)

        if block_type == BlockType.CODE:
            # Remove triple backticks but preserve ALL internal content including newlines
            code_content = block
            if code_content.startswith("```") and code_content.endswith("```"):
                # Slice between backticks, keeping all internal content exactly as-is
                code_content = code_content[3:-3]
                # Only remove the leading/trailing backtick lines if they're empty
                lines = code_content.splitlines(keepends=True)
                # Remove leading empty lines
                while lines and lines[0].strip() == "":
                    lines.pop(0)
                # Remove trailing empty lines EXCEPT for one final newline
                while (
                    len(lines) > 1
                    and lines[-1].strip() == ""
                    and lines[-2].strip() == ""
                ):
                    lines.pop(-1)
                code_content = "".join(lines)
            code_inner = ParentNode(
                "code", [TextNode(code_content, TextType.TEXT)], None
            )
            children.append(ParentNode("pre", [code_inner], None))
        else:
            # Handle non-code blocks
            block_text = " ".join(
                line.strip() for line in block.split("\n") if line.strip()
            )
            text_nodes = text_to_textnodes(block_text)
            html_nodes = [text_node_to_html_node(node) for node in text_nodes]

            if block_type == BlockType.PARAGRAPH:
                children.append(ParentNode("p", html_nodes, None))
            elif block_type == BlockType.HEADING:
                heading_level = block.count("#", 0, block.find(" "))
                tag = f"h{heading_level}"
                children.append(ParentNode(tag, html_nodes, None))
            elif block_type == BlockType.UNORDERED_LIST:
                list_items = [
                    ParentNode(
                        "li", [text_node_to_html_node(item.lstrip("-").strip())], None
                    )
                    for item in block.split("\n")
                    if item.strip()
                ]
                children.append(ParentNode("ul", list_items, None))
            elif block_type == BlockType.ORDERED_LIST:
                list_items = [
                    ParentNode(
                        "li",
                        [text_node_to_html_node(item.split(maxsplit=1)[-1].strip())],
                        None,
                    )
                    for item in block.split("\n")
                    if item.strip()
                ]
                children.append(ParentNode("ol", list_items, None))
            elif block_type == BlockType.QUOTE:
                children.append(ParentNode("blockquote", html_nodes, None))
            else:
                raise ValueError(f"Unhandled block type: {block_type}")

    return ParentNode("div", children, None)
