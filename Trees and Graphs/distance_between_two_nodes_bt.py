"""
Find the distance between the two nodes in binary tree
"""


class Tree:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right


def make_tree(index=0):
    if index == 0:
        '''
                      1
              2                3
          4                5          6
        7   8            9   10    11    12
                      15               14
        '''
        t1 = Tree(2, Tree(4, Tree(7), Tree(8)))
        t2 = Tree(5, Tree(9, Tree(15)), Tree(10))
        t3 = Tree(6, Tree(11), Tree(12, Tree(14)))
        t = Tree(1, t1, Tree(3, t2, t3))
        return t


def inorder_traversal(tree, path=None):
    if path is None:
        path = []
    if tree is not None:
        inorder_traversal(tree.left, path)
        path.append(tree.node)
        inorder_traversal(tree.right, path)
    return path


def find_distance(tree, nodes, path):
    if tree is not None:
        path.append(tree.node)
        if tree.node in nodes:
            nodes[tree.node] = path.copy()

        l = find_distance(tree.left, nodes, path)
        r = find_distance(tree.right, nodes, path)
        path.pop()


def get_distance(found, nodes):
    distance = 0
    i = j = 0
    while i < found[nodes[0]] and j < found[nodes[1]]:
        if found[nodes[0]][i] == found[nodes[1]][j]:
            i += 1
            j += 1

        else:
            break



def find_distance_between_nodes(tree, nodes):
    found = {node: False for node in nodes}
    find_distance(tree, found, [])
    print(found)
    if any([True if found[node] is False else False for node in found]):
        return False
    return get_distance(found, nodes)

tree = make_tree()
print(inorder_traversal(tree))


# nodes = [(8, 11), (1, 2), (1, 4), (6, 15), (3, 15), (9, 13), (0, 5), (15, 19), (14, 13), (-3, -9)]
nodes = [(2, 3), (4, 7), (3, 12)]

for node in nodes:
    print(node, '-', find_distance_between_nodes(tree, node))
