import re


def extract_title(markdown):
    matches = re.findall(r"(?<=#).*?([A-Z]\S+)|(?!^)\G.*?([A-Z]\S+)", markdown)
    title = ""
    for match in matches:
        title += match
    return matches
