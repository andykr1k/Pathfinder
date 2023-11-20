'''
node = array made out of image

'''

class Tree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        self.print_tree_helper(self.root)

    def print_tree_helper(self, node):
        node.print_node()

        if len(self.root.children) == 0:
            return
        
        for child in node.children:
            self.print_tree_helper(child)