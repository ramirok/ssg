import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a text node", "bold")
        node2 = HTMLNode("p","This is a text node", "bold")
        self.assertEqual(node.props_to_html(), node2.props_to_html())

        node3 = HTMLNode("p", "This is a text node", "bold", {"class": "test"})
        node4 = HTMLNode("p", "This is a text node", "bold", {"class": "test"})
        self.assertEqual(node3.props_to_html(), node4.props_to_html())


if __name__ == "__main__":
    unittest.main()