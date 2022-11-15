class HTMLNodeVisitor:
    def visit(self, node):
        node.accept(self)

    def visit_HTMLNode(self, node):
        for child in node.children:
            child.accept(self)

    def visit_UnknownHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_DocumentHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_HtmlHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_HeadHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_TitleHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_BaseHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_LinkHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_MetaHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_StyleHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_SectionsHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_BodyHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_ArticleHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_SectionHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_NavHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_AsideHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_HgroupHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_HeaderHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_FooterHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_AddresHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_PHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_HrHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_PreHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_BlockquoteHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_OlHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_UlHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_MenuHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_LiHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_DlHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_DtHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_DdHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_FigureHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_FigcaptionHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_MainHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_DivHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_AHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_EmHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_StrongHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_SmallHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_SHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_CiteHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_QHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_DfnHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_AbbrHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_RubyHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_RtHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_RpHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_DataHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_TimeHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_CodeHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_VarHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_SampHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_KbdHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_IHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_BHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_UHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_MarkHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_BdiHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_BdoHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_SpanHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_BrHTMLNode(self, node):
        self.visit_HTMLNode(node)

    def visit_WbrHTMLNode(self, node):
        self.visit_HTMLNode(node)
