from block_type import BlockType, block_to_block_type
from htmlnode import LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def main():
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text, None)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text, None)
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode(
                "img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"}
            )
        else:
            raise Exception

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

            block_type = block_to_block_type(block)

            # Handle code blocks separately (no inline parsing)
            if block_type == BlockType.CODE:
                code_content = block.strip()
                if code_content.startswith("```") and code_content.endswith("```"):
                    code_content = code_content[3:-3]
                    # Remove leading/trailing newlines but keep internal ones
                    code_content = code_content.strip("\n")
                html_nodes = [TextNode(code_content, TextType.TEXT)]
            else:
                block_text = " ".join(
                    line.strip() for line in block.split("\n") if line.strip()
                )
                text_nodes = text_to_textnodes(block_text)
                html_nodes = [text_node_to_html_node(node) for node in text_nodes]
                # Convert blocks to appropriate HTML structure
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

            elif block_type == BlockType.CODE:
                code_inner = ParentNode(
                    "code", [TextNode(block.strip(), TextType.TEXT)], None
                )
                children.append(ParentNode("pre", [code_inner], None))

            else:
                raise ValueError(f"Unhandled block type: {block_type}")

        return ParentNode("div", children, None)

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
