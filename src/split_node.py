from textnode import TextType, TextNode
from extract_links_images import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        remaining_text = node.text
        while delimiter in remaining_text:
            index_first = remaining_text.find(delimiter)
            index_second = remaining_text.find(delimiter, index_first + len(delimiter))

            if index_second == -1:
                raise Exception("invalid markdown syntax")

            text_before = remaining_text[:index_first]
            text_inside = remaining_text[index_first + len(delimiter) : index_second]
            remaining_text = remaining_text[index_second + len(delimiter) :]

            new_list.extend(
                [
                    TextNode(text_before, TextType.TEXT),
                    TextNode(text_inside, text_type),
                ]
            )

        if len(remaining_text) > 0:
            new_list.append(TextNode(remaining_text, TextType.TEXT))

    return new_list


def split_nodes_image(old_nodes):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            result.append(node)
            continue

        remaining_text = text
        for image_alt, image_url in images:
            image_markdown = f"![{image_alt}]({image_url})"
            parts = remaining_text.split(image_markdown, 1)

            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))

            result.append(TextNode(image_alt, TextType.IMAGE, image_url))

            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result


def split_nodes_link(old_nodes):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            result.append(node)
            continue

        remaining_text = text
        for link_alt, link_url in links:
            link_markdown = f"[{link_alt}]({link_url})"
            parts = remaining_text.split(link_markdown, 1)

            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))

            result.append(TextNode(link_alt, TextType.LINK, link_url))

            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result
