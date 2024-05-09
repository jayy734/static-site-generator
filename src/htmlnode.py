class HTMLNode:
    def __init__(self,tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError("This should be implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        output = ""
        for key , value in self.props.items():
            output += " " + (f'{key}="{value}"') 
        return output
        
    def __repr__(self):
        return f"tag = {self.tag} , value = {self.value}, children = {self.children}, props = {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props={}):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode requires a value")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children = [], props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag should be provided!")
        if self.children == None:
            raise ValueError("ParentNode must have children!")
        result = ""
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

    
node = LeafNode("p", "This is a paragraph of text.")
node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
node3 = HTMLNode(None, None, None , {"href": "https://www.google.com", "target": "_blank"})
node4 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)



print(node.to_html())
print(node2.to_html())
print(node3.props_to_html())
print(node4.to_html())
