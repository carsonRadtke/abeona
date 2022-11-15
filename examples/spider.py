#!/usr/bin/env python3

# ./spider.py \
#   --start https://en.wikipedia.org/wiki/The_Starting_Line \
#   --depth 1

import argparse
import sys
import requests

from context import abeona


class SpiderVisitor(abeona.visitors.HTMLNodeVisitor):
    def visit_AHTMLNode(self, node):
        super().visit_AHTMLNode(node)
        print(node.attributes.get("href", None))


class Spider:
    def __init__(self, start):
        self.to_visit = set()
        self.to_visit.add(start)
        self.visited = set()

    @staticmethod
    def get_links(contents):
        document = abeona.parser.AbeonaParser().get_document(contents)
        visitor = SpiderVisitor()
        visitor.visit(document)
        return []

    def visit(self, url):
        if url in self.visited:
            return
        self.visited.add(url)
        print("visiting " + url)
        res = requests.get(url)
        if res.status_code == 200:
            contents = res.text
            for link in Spider.get_links(contents):
                self.to_visit.add(link)

    def begin(self):
        while len(self.to_visit) > 0:
            self.visit(self.to_visit.pop())


def spider_main(args):
    spider = Spider(args.start)
    spider.begin()
    return 0


def main():
    ap = argparse.ArgumentParser(
        prog="spider",
        description="spiders the internet from root url",
        add_help=True,
        exit_on_error=True,
    )
    ap.add_argument(
        "--start", help="Where to start the spider", required=True, type=str
    )
    ap.add_argument(
        "--depth",
        help="How many links to click per path",
        required=False,
        type=int,
        default=3,
    )
    return spider_main(ap.parse_args())


if __name__ == "__main__":
    sys.exit(main())
