from Tree import Tree
from TreeNode import TreeNode
from collections import deque

def BFS(node):
    node.print_node()

    if (len(node.children) == 0):
        return
    
    []

def DFS(node):
    node.print_node()

    if (len(node.children) == 0):
        return

    for child in node.children:
        DFS(child)

def main():
    i = [1,1,1]
    j = [0,0,0]
    x = [1,0,0]
    z = [1,0,1]

    root = TreeNode(i)
    tree = Tree(root)    
    node1 = TreeNode(j)
    root.add_child(node1)
    node2 = TreeNode(x)
    node3 = TreeNode(z)
    node1.add_child(node3)
    node1.add_child(node2)
    # tree.print_tree()
    # DFS(root)
    BFS(root)
    
if __name__ == '__main__':
    main()
