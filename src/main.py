from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from split_node import split_nodes_delimiter, split_nodes_link, split_nodes_image
from text_to_html import text_node_to_html_node


def main():

    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and an ![image](www.image_source.com)",
        TextType.TEXT,
    )

    new_nodes = split_nodes_link([node])

    final_nodes = split_nodes_image(new_nodes)

    print(final_nodes)


if __name__ == "__main__":
    main()
