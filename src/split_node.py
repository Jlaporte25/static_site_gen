from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)

        text_before, text_inside, text_after = node.text.split(delimiter)
        new_list.extend(
            [
                TextNode(text_before, TextType.TEXT),
                TextNode(text_inside, text_type),
                TextNode(text_after, TextType.TEXT),
            ]
        )

    return new_list
