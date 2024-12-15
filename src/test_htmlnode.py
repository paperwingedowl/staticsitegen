import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        node = HTMLNode("a", "b")
        node2 = HTMLNode("a", "b", None, None)
        self.assertNotEqual(node, node2)

    def test2(self):
        node = HTMLNode("a", "b", "c")
        node2 = HTMLNode("a", "b", None, None)
        self.assertNotEqual(node, node2)

    def test3(self):
        node = HTMLNode("a", "b")
        node2 = HTMLNode("a", "b")
        string1 = node.props_to_html()
        string2 = node2.props_to_html()
        self.assertEqual(string1, string2)

if __name__ == "__main__":
    unittest.main()