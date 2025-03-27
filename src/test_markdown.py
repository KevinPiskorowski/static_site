import unittest

from textnode import TextNode, TextType

from markdown import (split_nodes_delimiter, extract_markdown_images, extract_markdown_links)

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This has a **bolded** word", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual([TextNode("This has a ", TextType.TEXT),
                              TextNode("bolded", TextType.BOLD),
                              TextNode(" word", TextType.TEXT)]
                              , new_node)
        

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://boot.dev)")
        self.assertListEqual([("link", "https://boot.dev")], matches)

    