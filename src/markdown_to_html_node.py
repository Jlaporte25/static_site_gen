from block_type import BlockType, block_to_block_type
from htmlnode import LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_to_html import text_node_to_html_node
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    if not isinstance(markdown, str):
        raise ValueError("Input must be a string")

    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        if not block.strip():
            continue

        block_type = block_to_block_type(block)

        try:
            if block_type == BlockType.CODE:
                code_content = block
                if code_content.startswith("```") and code_content.endswith("```"):
                    code_content = code_content[3:-3]
                    lines = code_content.splitlines(keepends=True)
                    while lines and not lines[0].strip():
                        lines.pop(0)
                    while (
                        len(lines) > 1
                        and not lines[-1].strip()
                        and not lines[-2].strip()
                    ):
                        lines.pop(-1)
                    code_content = "".join(lines)

                code_inner = ParentNode("code", [LeafNode(None, code_content)], None)
                children.append(ParentNode("pre", [code_inner], None))

            else:
                if block_type == BlockType.QUOTE:
                    lines = [
                        line.lstrip(">").strip()
                        for line in block.split("\n")
                        if line.strip()
                    ]
                else:
                    lines = [line.strip() for line in block.split("\n") if line.strip()]
                block_text = (
                    "\n".join(lines)
                    if block_type == BlockType.QUOTE
                    else " ".join(lines)
                )

                text_nodes = text_to_textnodes(block_text)
                html_nodes = [text_node_to_html_node(node) for node in text_nodes]

                if block_type == BlockType.PARAGRAPH:
                    children.append(ParentNode("p", html_nodes, None))
                elif block_type == BlockType.HEADING:
                    heading_level = min(block.count("#", 0, block.find(" ")), 6)
                    tag = f"h{heading_level}"
                    content_start = block.find(" ") + 1
                    cleaned_nodes = text_to_textnodes(block[content_start:].strip())
                    html_nodes = [
                        text_node_to_html_node(node) for node in cleaned_nodes
                    ]
                    children.append(ParentNode(tag, html_nodes, None))
                elif block_type == BlockType.UNORDERED_LIST:
                    list_items = []
                    for item in block.split("\n"):
                        if not item.strip():
                            continue
                        try:
                            # Handle case where bold text ends with colon
                            item_text = item.lstrip("- *").strip()
                            if item_text.startswith("**") and ":" in item_text:
                                # Split at first colon after bold opening
                                bold_end = item_text.find(":", item_text.find("**") + 2)
                                if (
                                    bold_end != -1
                                    and item_text[bold_end - 2 : bold_end] != "**"
                                ):
                                    # Insert closing ** before colon if not present
                                    item_text = (
                                        item_text[:bold_end]
                                        + "**"
                                        + item_text[bold_end:]
                                    )
                            if item_text:
                                nodes = text_to_textnodes(item_text)
                                html_nodes = [
                                    text_node_to_html_node(node) for node in nodes
                                ]
                                list_items.append(ParentNode("li", html_nodes, None))
                        except Exception as e:
                            raise ValueError(
                                f"Error processing list item '{item}': {str(e)}"
                            )
                    children.append(ParentNode("ul", list_items, None))
                elif block_type == BlockType.ORDERED_LIST:
                    list_items = []
                    for item in block.split("\n"):
                        if not item.strip():
                            continue
                        try:
                            item_text = item.split(".", maxsplit=1)[1].strip()
                            if item_text:
                                nodes = text_to_textnodes(item_text)
                                html_nodes = [
                                    text_node_to_html_node(node) for node in nodes
                                ]
                                list_items.append(ParentNode("li", html_nodes, None))
                        except Exception as e:
                            raise ValueError(
                                f"Error processing ordered list item '{item}': {str(e)}"
                            )
                    children.append(ParentNode("ol", list_items, None))
                elif block_type == BlockType.QUOTE:
                    children.append(ParentNode("blockquote", html_nodes, None))
                else:
                    raise ValueError(f"Unhandled block type: {block_type}")

        except Exception as e:
            raise ValueError(
                f"Error processing markdown block:\n{block}\n\nError: {str(e)}"
            )

    return ParentNode("div", children, None)
