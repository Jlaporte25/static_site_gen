from block_type import BlockType, block_to_block_type
from htmlnode import LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
import os
import shutil


def main():
    def copy_public_dir(path):
        if os.path.exists("public"):
            shutil.rmtree("public")
        os.mkdir("public")
        dirs = os.listdir("static")
        for dir in dirs:
            full_path = os.path.join(dir, path)
            if os.path.isfile(full_path):
                shutil.copy(full_path, "public")
            elif os.path.isdir(full_path):
                new_path = os.path.join(full_path, path)
                copy_public_dir(new_path)

    copy_public_dir("static")


if __name__ == "__main__":
    main()
