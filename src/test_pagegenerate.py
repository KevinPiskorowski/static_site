import unittest

from pagegenerate import extract_title

class TestPageGeneration(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_extract_title_long(self):
        md = """
# The title text

and now the regular text
        
        """
        title = extract_title(md)
        self.assertEqual(title, "The title text")
    