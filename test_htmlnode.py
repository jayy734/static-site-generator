import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node2 = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        node = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node2.props_to_html(), node)

if __name__ == "__main__":
    unittest.main()
