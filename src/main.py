from textnode import TextNode
from leafnode import LeafNode
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("Invalid type of text node")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        match text_type:
            case "code":
                splitted_text = node.text.split(delimiter)
                print(list(map(lambda x: TextNode(x, "code" if x[0] != "" else "text"), splitted_text)))
                return 
        raise Exception("Invalid type of text node")

node = TextNode("This is text with a `code block` word", "text")
new_nodes = split_nodes_delimiter([node], "`", "code")


def main():
    text_node = TextNode("hello", "bold", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

main()