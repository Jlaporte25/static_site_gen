from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    elif block.startswith(">"):
        return BlockType.QUOTE

    elif block.startswith("-"):
        return BlockType.UNORDERED_LIST

    elif re.match(r"^[0-9]+\. ", block):
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH
