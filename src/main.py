from textnode import *
from htmlnode import *

def main():
    testnode = TextNode("here's a picture of my giant donger", TextType.IMAGE, "http://www.mydonger.dong/pp.jpg")
    print(testnode)

    testdict = {
        "ass": "penis",
        "dick": "balls",
        "butt": "hole"
        }
    htmlnode = HTMLNode(None, None, None, testdict)
    print(htmlnode.props_to_html())
    print(htmlnode)
    
main()