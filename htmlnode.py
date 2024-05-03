class HTMLNode:
    def __init__(self,props= {} ):
        ## self.tag = tag
        #self.value = value
        #self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This should be implemented")
    
    def props_to_html(self):
        output = ""
        for key , value in self.props.items():
            output += " " + (f'{key}="{value}"') 
        return output
        
    def __repr__(self):
        return f"tag = {self.tag} , value = {self.value}, children = {self.children}, props = {self.props}"
    
