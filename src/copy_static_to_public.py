import os
import shutil


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
