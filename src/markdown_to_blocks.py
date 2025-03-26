def markdown_to_blocks(markdown):
    split_mark = markdown.split("\n\n")
    new_list = []
    for mark in split_mark:
        if len(mark) > 0:
            stripped = mark.strip()
            final = stripped.replace("  ", "")
            new_list.append(final)

    return new_list
