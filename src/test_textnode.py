import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_2(self):
        node = TextNode("this textnode so big", TextType.IMAGE, "http://www.bigtextnode.net")
        node2 = TextNode("this textnode so big", TextType.IMAGE, "http://www.bigtextnode.net")
        self.assertEqual(node, node2)
    
    #def test_3(self):
        #node = TextNode("this textnode so big", TextType.IMAGE, "http://www.bigtextnode.net")
        #node2 = TextNode("This TextNode So Big", TextType.IMAGE, "http://www.bigtextnode.net")
        #self.assertEqual(node, node2)

    def test_4(self):
        node = TextNode("wowow", TextType.NORMAL_TEXT, None)
        node2 = TextNode("wowow", TextType.NORMAL_TEXT)
        self.assertEqual(node, node2)
    
    #def test_5(self):
        #node = TextNode("penis", TextType.ITALIC_TEXT)
        #node2 = TextNode("penis", TextType.BOLD_TEXT)
        #self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()