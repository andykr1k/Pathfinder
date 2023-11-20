'''
node = array made out of image

'''

class TreeNode:
    def __init__(self, img):
        self.data = img # image array of node
        self.children = {}

    def add_child(self, node):
        child_data = {
            "fmove" : self.generate_forward_movement(node), # Generate Forward Movement Function Here
            "bmove" : self.generate_backward_movement(node) # Generate Backward Movement Function Here
        }
        self.children[node] = child_data

    def print_node(self):
        print(self.data)

    def generate_forward_movement(self, node):
        return 1
    
    def generate_backward_movement(self, node):
        return -1