import unittest
from block_type import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_block(self):
        block = "## This is a heading"
        bl_type = block_to_block_type(block)
        self.assertEqual(bl_type, BlockType.HEADING)

    def test_block_code(self):
        block = "-this is item one\n- this is item two"
        bl_type = block_to_block_type(block)
        self.assertEqual(bl_type, BlockType.UNORDERED_LIST)
