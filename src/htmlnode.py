class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return None
        full_string = ""
        for key, val in self.props.items():
            if full_string == "":
                full_string += f'{key}="{val}"'
            else:
                full_string += f' {key}="{val}"'
        return full_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"