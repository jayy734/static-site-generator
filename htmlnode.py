class HTMLNode:
    def __init__(self,tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError("This should be implemented")
    
    def props_to_html(self):
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
    
node = LeafNode("p", "This is a paragraph of text.")
node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
node3 = HTMLNode(None, None, None , {"href": "https://www.google.com", "target": "_blank"})

print(node.to_html())
print(node2.to_html())
print(node3.props_to_html())
