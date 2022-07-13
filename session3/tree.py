class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    

def pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            visit_order.append(node)
            traverse(node.get_left_child())
            traverse(node.get_right_child())
    
    traverse(root)
    return visit_order

def in_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visit_order.append(node)
            traverse(node.get_right_child())
    
    traverse(root)
    return visit_order

def post_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visit_order.append(node)
    
    traverse(root)
    return visit_order





if __name__ == "__main__":
    tree = Tree("F")
    tree.get_root().set_left_child(Node("B"))
    tree.get_root().get_left_child().set_left_child(Node("A"))
    tree.get_root().get_left_child().set_right_child(Node("D"))
    tree.get_root().get_left_child().get_right_child().set_right_child(Node("E"))
    tree.get_root().get_left_child().get_right_child().set_left_child(Node("C"))

    tree.get_root().set_right_child(Node("G"))
    tree.get_root().get_right_child().set_right_child(Node("I"))
    tree.get_root().get_right_child().get_right_child().set_left_child(Node("H"))
    # print(pre_order(tree))
    # print("In-Order", in_order(tree))
    print("Post-Order", post_order(tree))