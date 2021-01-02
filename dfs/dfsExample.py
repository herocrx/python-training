

from collections import deque

class Node:
    def __init__(self, number):
        self.number = number
        self.children = list()
        

    def addChild(self, n):
        self.children.append(n)


def dfs(currentNode, visited):
    print('Executing node: ', currentNode.number)
    visited.add(currentNode)

    for node in currentNode.children:
        if node not in visited:
            dfs(node, visited)

def execute():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)

    n1.addChild(n2)
    n1.addChild(n9)
    n2.addChild(n3)
    n3.addChild(n4)
    n4.addChild(n5)
    n5.addChild(n6)
    n6.addChild(n7)
    n7.addChild(n8)
    n7.addChild(n1)
    n8.addChild(n9)


    visited = set()
    dfs(n1, visited)


execute()