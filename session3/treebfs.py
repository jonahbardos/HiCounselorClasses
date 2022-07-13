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

""
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
    
    def peek(self):
        if len(self.items) > 0:
            print(self.items)
            return self.items[0].value
    
    def __repr__(self):
        return f"{self.items}"
    def __str__(self):
        return f"{self.items}"
    

class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def level_order(self, start): #BFS (ITeration)
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)
        traversal = []

        while len(queue.items) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            
            if node.right:
                queue.enqueue(node.right)
        
        return traversal
    
    def get_height(self, start): # Homework
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)
        levels = []
        levels.append(start)
        level = 0

        while len(queue.items) != 0:
            
            newQueue = Queue()
            for node in queue.items:
                if node.left:
                    newQueue.enqueue(node.left)
            
                if node.right:
                    newQueue.enqueue(node.right)

            if len(newQueue.items):
                levels.append(newQueue)

            queue = newQueue
            level += 1
        
        print(level - 1)
        return levels





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
    tree.get_root().get_right_child().get_right_child().get_left_child().set_left_child(Node("J"))

    print(tree.level_order(tree.get_root()))
    # print(tree.get_height(tree.get_root()))
    # print(tree.get_height(tree.get_root().get_right_child()))