"""The HTML Parser. Responsible for taking HTML contents and building
an AST.
"""

from typing import List, Tuple

import html.parser

from . import stack
from ..nodes import HTMLNode, UnknownHTMLNode


class AbeonaParser(html.parser.HTMLParser):
    """An HTML parser that constructs an HTML AST.
    Attributes:
        `node_stack`: `stack.Stack` - keeps track of nested elements
    """

    @staticmethod
    def __format_tag(tag: str) -> str:
        """Takes a tag and converts it to match `[A-Z][a-z]*`
        Arguments:
            `tag`: `str` - the tag string to be formatted
        Returns:
            `str` - the capitalized tag string
        """
        res = list(tag.lower())
        res[0] = chr(ord(res[0]) - ord("a") + ord("A"))
        return "".join(res)

    @staticmethod
    def __build_html_node(tag: str, attrs: List[Tuple[str, str]]) -> HTMLNode:
        """Constructs an HTMLNode based on `tag`. If a known tag is found,
        it will be an instance of that HTMLNode, otherwise it will be
        `UnknownHTMLNode`.
        Arguments:
            `tag`: `str` - the element's tag
            `attrs`: `List[Tuple[str, str]] - the elements' attributes
        Returns:
            `HTMLNode` - the newly constructed HTMLNode
        """
        f_tag = AbeonaParser.__format_tag(tag) + "HTMLNode"
        try:
            return globals()[f_tag](attrs)
        except:
            return UnknownHTMLNode(tag, attrs)

    def __init__(self) -> None:
        root_html_node = AbeonaParser.__build_html_node("document", [])
        self.node_stack = stack.Stack()
        self.node_stack.push(root_html_node)
        html.parser.HTMLParser.__init__(self)

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str]]) -> None:
        parent = self.node_stack.peek()
        new_child = AbeonaParser.__build_html_node(tag, attrs)
        parent.add_child(new_child)
        self.node_stack.push(new_child)

    def handle_endtag(self, tag) -> None:
        _ = self.node_stack.pop()

    def handle_data(self, data: str) -> None:
        self.node_stack.peek().set_text(data)

    def get_document(self, contents: str) -> HTMLNode:
        self.feed(contents)
        return self.node_stack.peek()
