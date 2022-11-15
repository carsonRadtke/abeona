from ..visitors import HTMLNodeVisitor
from typing import List, Tuple, Dict

class HTMLNode:
    """Abstraction of an HTML DOM element."""

    def __init__(self, attributes: List[Tuple[str, str]]) -> None:
        """Create an HTMLNode object.
        Arguments:
            `attributes`: `List[Tuple[str,str]]` - corresponds to the elemnts' attributes
        """
        self.attributes: Dict[str, str] = dict(attributes)
        self.text: str = None
        self.children: List["HTMLNode"] = []

    def get_tag(self) -> str:
        """Get the tag associated with an element.
        Returns:
            `str` - the element's tag
        """
        name = self.__class__.__name__
        namel = len(name)
        return name[: namel - len("HTMLNode")].lower()

    def set_text(self, text: str) -> None:
        """Sets the contents of an element.
        Arguments:
            `text`: `str` - the textual contents of the element
        """
        self.text = text

    def add_child(self, child: "HTMLNode") -> None:
        """Adds an HTMLNode as a child of an element
        Arguments:
            `child`: `HTMLNode` - the child to add
        """
        self.children.append(child)

    def accept(self, visitor: HTMLNodeVisitor) -> None:
        """Accept a visitor's visit.
        Arguments:
            `visitor`: `HTMLNodeVisitor` - the visitor that is visiting
        """
        getattr(visitor, f"visit_{self.__class__.__name__}")(self)


class UnknownHTMLNode(HTMLNode):
    """An HTMLNode that we don't model"""
    def __init__(self, tag: str, attributes: List[Tuple[str,str]]) -> None:
        """Create an HTMLNode object.
        Arguments:
            `tag`: `str` - the UnknownHTMLNode's tag
            `attributes`: `List[Tuple[str,str]]` - corresponds to the elemnts' attributes
        """
        super().__init__(attributes)
        self.tag = tag

    def get_tag(self) -> str:
        return self.tag

    def accept(self, visitor: HTMLNodeVisitor) -> None:
        visitor.visit_UnknownHTMLNode(self)

# The following nodes came from:
# https://html.spec.whatwg.org/#toc-semantics (11/13/22)
#  - carsonRadtke

class DocumentHTMLNode(HTMLNode):
    pass


class HtmlHTMLNode(HTMLNode):
    pass


class HeadHTMLNode(HTMLNode):
    pass


class TitleHTMLNode(HTMLNode):
    pass


class BaseHTMLNode(HTMLNode):
    pass


class LinkHTMLNode(HTMLNode):
    pass


class MetaHTMLNode(HTMLNode):
    pass


class StyleHTMLNode(HTMLNode):
    pass


class SectionsHTMLNode(HTMLNode):
    pass


class BodyHTMLNode(HTMLNode):
    pass


class ArticleHTMLNode(HTMLNode):
    pass


class SectionHTMLNode(HTMLNode):
    pass


class NavHTMLNode(HTMLNode):
    pass


class AsideHTMLNode(HTMLNode):
    pass


class HgroupHTMLNode(HTMLNode):
    pass


class HeaderHTMLNode(HTMLNode):
    pass


class FooterHTMLNode(HTMLNode):
    pass


class AddresHTMLNode(HTMLNode):
    pass


class PHTMLNode(HTMLNode):
    pass


class HrHTMLNode(HTMLNode):
    pass


class PreHTMLNode(HTMLNode):
    pass


class BlockquoteHTMLNode(HTMLNode):
    pass


class OlHTMLNode(HTMLNode):
    pass


class UlHTMLNode(HTMLNode):
    pass


class MenuHTMLNode(HTMLNode):
    pass


class LiHTMLNode(HTMLNode):
    pass


class DlHTMLNode(HTMLNode):
    pass


class DtHTMLNode(HTMLNode):
    pass


class DdHTMLNode(HTMLNode):
    pass


class FigureHTMLNode(HTMLNode):
    pass


class FigcaptionHTMLNode(HTMLNode):
    pass


class MainHTMLNode(HTMLNode):
    pass


class DivHTMLNode(HTMLNode):
    pass


class AHTMLNode(HTMLNode):
    pass


class EmHTMLNode(HTMLNode):
    pass


class StrongHTMLNode(HTMLNode):
    pass


class SmallHTMLNode(HTMLNode):
    pass


class SHTMLNode(HTMLNode):
    pass


class CiteHTMLNode(HTMLNode):
    pass


class QHTMLNode(HTMLNode):
    pass


class DfnHTMLNode(HTMLNode):
    pass


class AbbrHTMLNode(HTMLNode):
    pass


class RubyHTMLNode(HTMLNode):
    pass


class RtHTMLNode(HTMLNode):
    pass


class RpHTMLNode(HTMLNode):
    pass


class DataHTMLNode(HTMLNode):
    pass


class TimeHTMLNode(HTMLNode):
    pass


class CodeHTMLNode(HTMLNode):
    pass


class VarHTMLNode(HTMLNode):
    pass


class SampHTMLNode(HTMLNode):
    pass


class KbdHTMLNode(HTMLNode):
    pass


class IHTMLNode(HTMLNode):
    pass


class BHTMLNode(HTMLNode):
    pass


class UHTMLNode(HTMLNode):
    pass


class MarkHTMLNode(HTMLNode):
    pass


class BdiHTMLNode(HTMLNode):
    pass


class BdoHTMLNode(HTMLNode):
    pass


class SpanHTMLNode(HTMLNode):
    pass


class BrHTMLNode(HTMLNode):
    pass


class WbrHTMLNode(HTMLNode):
    pass
