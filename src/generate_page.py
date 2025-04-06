from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path, "r")
    from_markdown = f.read()
    f.close()

    f = open(template_path, "r")
    template_html = f.read()
    f.close()

    node = markdown_to_html_node(from_markdown)
    html = node.to_html()
    title = extract_title(from_markdown)

    template_with_title = template_html.replace("{{ Title }}", title)
    template_final = template_with_title.replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    f = open(dest_path, "w")
    f.write(template_final)
    f.close()
