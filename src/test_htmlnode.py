import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_HTML_props(self):
        node = HTMLNode("tag", "value", None,{"class": "greeting", "href": "https://boot.dev"}, )
        self.assertEqual(node.props_to_html(), ' class="greeting" href="https://boot.dev"')
    
    def test_repr(self):
        node = HTMLNode("p", "what the hecc", None, {"class" : "primary"},)
        self.assertEqual(node.__repr__(), "HTMLNode(p, what the hecc, children: None, {'class': 'primary'})")

    def test_values(self):
        node = HTMLNode("div", "help",)
        self.assertEqual(node.tag, "div")

        self.assertEqual(node.value, "help")
    
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is not a jumpscare", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">This is not a jumpscare</a>')
    def test_leaf_to_html_none(self):
        node = LeafNode(None, "This shouldn't have a tag")
        self.assertEqual(node.to_html(), "This shouldn't have a tag")

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode("a", [LeafNode(None, "This is a child"), LeafNode("b", "This is a bold child")])
        self.assertEqual(node.to_html(), f'<a>This is a child<b>This is a bold child</b></a>' )
    


if __name__ == "__main__":
    unittest.main()