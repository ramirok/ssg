import unittest
from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p")


if __name__ == "__main__":
    unittest.main()