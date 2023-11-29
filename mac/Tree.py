'''
node = array made out of image

'''

class Tree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        if self.root is None:
            return

        queue = [self.root]
        layer = 1

        while len(queue) > 0:
            cur_node = queue.pop(0)
            cur_node.print_node()

            if len(cur_node.children) > 0:
                for child in cur_node.children:
                    queue.append(child)