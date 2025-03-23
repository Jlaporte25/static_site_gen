import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode(
            "p",
            "this is the text inside the tag",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertIsInstance(html_node.props_to_html(), str)

    def test_props_to_html_2(self):
        html_node_2 = HTMLNode("h1", "This is the title", None, None)

        self.assertNotIsInstance(html_node_2.props_to_html(), dict)

    def test_props_to_html_3(self):
        html_node = HTMLNode(
            "p",
            "this is the text inside the tag",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertIsInstance(html_node.props_to_html(), str)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a", "Click Here", {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank">Click Here</a>',
        )
