from typing import Required


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        for key, value in self.props.items():
            html = html + f' {key}="{value}"'
        return html

    def __repr__(self):
        return f"HTMLNode:(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=Required, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
