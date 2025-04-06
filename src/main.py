from generate_page import generate_page
import os
import shutil


def main():
    def copy_static_to_public(source_dir, dest_dir):
        # Initial cleanup
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)
        os.mkdir(dest_dir)

        # Now copy files and directories
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            dest_item = os.path.join(dest_dir, item)

            if os.path.isfile(source_item):
                # What should happen with files?
                shutil.copy(source_item, dest_item)
            elif os.path.isdir(source_item):
                # What should happen with directories?
                copy_static_to_public(source_item, dest_item)

    copy_static_to_public("static", "public")

    content_dir = "content"
    public_dir = "public"

    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                output_path = file_path.replace(content_dir, public_dir).replace(
                    ".md", ".html"
                )
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                generate_page(file_path, "template.html", output_path)


if __name__ == "__main__":
    main()
