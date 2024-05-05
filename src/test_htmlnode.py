import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node2 = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        node = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node2.props_to_html(), node)

    def test_parentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(),node2)
        
    def test_nested_children(self):
        grandchild_node = LeafNode("b","grandchild")
        child_node = ParentNode("div",[grandchild_node])
        node = ParentNode("b" , [child_node])
        result = "<b><div><b>grandchild</b></div></b>"
        self.assertEqual(node.to_html(),result)


if __name__ == "__main__":
    unittest.main()
