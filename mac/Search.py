def BFS(node):
    if node is None:
        return
    queue = [node]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        cur_node.print_node()

        if len(cur_node.children) > 0:
            for child in cur_node.children:
                queue.append(child)

def DFS(node):
    node.print_node()

    if (len(node.children) == 0):
        return

    for child in node.children:
        DFS(child)