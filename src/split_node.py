from textnode import TextType, TextNode


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
