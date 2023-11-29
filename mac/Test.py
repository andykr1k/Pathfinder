from Tree import Tree
from TreeNode import TreeNode
from Search import DFS, BFS

def FakeTree():
    i = [1,1,1]
    j = [0,0,0]
    x = [1,0,0]
    z = [1,0,1]
    a = [0,0,2]
    b = [0,2,0]
    c = [2,0,0]
    root = TreeNode(i)
    tree = Tree(root)
    node1 = TreeNode(j)
    root.add_child(node1)
    node2 = TreeNode(x)
    node3 = TreeNode(z)
    node1.add_child(node2)
    node1.add_child(node3)
    node4 = TreeNode(a)
    node5 = TreeNode(b)
    node6 = TreeNode(c)
    node2.add_child(node4)
    node2.add_child(node5)
    node3.add_child(node6)

    return tree

def TestAlgos():
    tree = FakeTree()

    print("Printing Tree")
    tree.print_tree()

    print("DFS Algorithm")
    DFS(tree.root)

    print("BFS Algorithm")
    BFS(tree.root)