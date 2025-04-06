from generate_page import generate_page
from copy_static_to_public import copy_static_to_public
import os
import sys


def main():
    copy_static_to_public("static", "docs")

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    content_dir = "content"
    docs_path = "docs"

    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                output_path = file_path.replace(content_dir, docs_path).replace(
                    ".md", ".html"
                )
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                generate_page(file_path, "template.html", output_path, basepath)


if __name__ == "__main__":
    main()
