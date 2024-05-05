from htmlnode import LeafNode

text_types = {"text": lambda text_node: LeafNode(None, text_node.text),
              "bold": lambda text_node: LeafNode("b" , text_node.text),
              "italic": lambda text_node: LeafNode("i", text_node.text),
              "code": lambda text_node: LeafNode("code",text_node.text),
              "link": lambda text_node: LeafNode("a", text_node.text , {"href": text_node.url}),
              "image": lambda text_node: LeafNode("img","", {"src": text_node.url , "alt": text_node.text})
}



class TextNode:
    def __init__(self , text , text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self , other):
        return (
            self.text == other.text 
            and self.text_type == other.text_type
            and self.url == other.url
        )
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(text_node):
        if text_node.text_type not in text_types:
            raise Exception("Not a valid text type!")
        return text_types[text_node.text_type](text_node)
        
 