class Node:
    def __init__(self, value):
        self.value = value
        self.adjecent_list = []

        # By default all the nodes are not visited
        # We set to True when we visit a Node
        self.visted = False 
    

class Graph:
    def BFS(self, node):
        queue = []
        queue.append(node)
        node.visted = True

        traversal = []

        while queue:
            actualNode = queue.pop(0)
            traversal.append(actualNode.value)
            
            for element in actualNode.adjecent_list:
                if element.visted is False:
                    queue.append(element)
                    element.visted = True

        return traversal   
    
    def DFS(self, node, traversal):
        node.visted = True
        traversal.append(node.value)

        for element in node.adjecent_list: # Use to check all its adjacent nodes
            if element.visted is False:
                self.DFS(element, traversal)

        return traversal



if __name__ == "__main__":
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")

    # Node A
    nodeA.adjecent_list.append(nodeB)
    nodeA.adjecent_list.append(nodeC)
    nodeA.adjecent_list.append(nodeD)

    # Node B
    nodeB.adjecent_list.append(nodeE)
    nodeB.adjecent_list.append(nodeF)

    # Node D
    nodeD.adjecent_list.append(nodeG)

    graph = Graph()
    # print(graph.BFS(nodeA))
    print(graph.DFS(nodeA, []))