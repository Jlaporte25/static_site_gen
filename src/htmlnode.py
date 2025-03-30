from textnode import TextNode


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}

    def to_html(self) -> str:
        pass

    def props_to_html(self):
        html = ""
        for key, value in self.props.items():
            html = html + f' {key}="{value}"'
        return html

    def __repr__(self):
        return f"HTMLNode:(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return f"{self.value}"
        elif self.props is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("no tag")
        elif self.children is None:
            raise ValueError("no children")
        else:
            children = ""
            for child in self.children:
                if isinstance(child, TextNode):
                    children += child.text
                else:
                    children += child.to_html()
            return f"<{self.tag}>{children}</{self.tag}>"
