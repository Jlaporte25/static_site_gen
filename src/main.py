from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    test_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(test_node)

    html_node = HTMLNode(
        "p", "this is the text inside the tag", None, {"href": "https://www.google.com"}
    )
    print(html_node)


if __name__ == "__main__":
    main()
