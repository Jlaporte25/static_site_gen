import unittest
from split_node import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNode(unittest.TestCase):
    def test_split_node_bold(self):
        node = TextNode("this is a string with a **bold** word", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            nodes,
            [
                TextNode("this is a string with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_node_bold_2(self):
        node = TextNode("this is a **string** with a **bold** word", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            nodes,
            [
                TextNode("this is a ", TextType.TEXT),
                TextNode("string", TextType.BOLD),
                TextNode(" with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )
