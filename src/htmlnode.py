class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key in self.props:
            html_addition = f' {key}="{self.props[key]}"'
            props_html += html_addition
        return props_html

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f'{self.value}'
        props = self.props_to_html()   
        return f'<{self.tag}{props}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("HTML Error: Missing Tag")
        if self.children is None:
            raise ValueError("HTML Error: Children Required")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
            





        

