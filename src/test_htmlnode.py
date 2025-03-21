import unittest
from htmlnode import HTMLNode


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
