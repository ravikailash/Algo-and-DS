"""
Finding the distance between the two nodes in binary search tree
"""

class Tree:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right


def make_tree(index=0):
    if index == 0:
        '''
                      5                     <- root node
              4                10
          2                8         12
        1   3            7   9    11     15
                      6                13
        '''
        t1 = Tree(4, Tree(2, Tree(1), Tree(3)))
        t2 = Tree(8, Tree(7, Tree(6)), Tree(9))
        t3 = Tree(12, Tree(11), Tree(15, Tree(13)))
        t = Tree(5, t1, Tree(10, t2, t3))
        return t


def inorder_traversal(tree, path=None):
    if path is None:
        path = []
    if tree is not None:
        inorder_traversal(tree.left, path)
        path.append(tree.node)
        inorder_traversal(tree.right, path)
    return path


def find_root_node(tree, nodes):
    if tree is None:
        return None
    if tree.node < min(nodes):
        return find_root_node(tree.right, nodes)
    elif tree.node > max(nodes):
        return find_root_node(tree.left, nodes)
    return tree

def find_distance(tree, node, path):
    if tree is None:
        return False

    if tree is not None:
        if tree.node == node:
            return path
        path += 1
        if tree.node < node:
            return find_distance(tree.right, node, path)
        else:
            return find_distance(tree.left, node, path)

def find_distance_between_nodes(tree, nodes):
    root_node = find_root_node(tree, nodes)

    if root_node is None:
        return False

    distance = 0
    if root_node.node in nodes:
        visit_node = nodes[0] if root_node.node == nodes[1] else nodes[1]
        distance = find_distance(root_node, visit_node, 0)
    else:
        n1_distance = find_distance(root_node, nodes[0], 0)
        n2_distance = find_distance(root_node, nodes[1], 0)
        if n1_distance is False or n2_distance is False:
            distance = False
        else:
            distance = n1_distance + n2_distance
    return distance


tree = make_tree()
print('Inorder Traversal: ', inorder_traversal(tree))


nodes = [(8, 11), (1, 2), (1, 4), (6, 15), (3, 15), (9, 13), (0, 5), (15, 19), (14, 13), (-3, -9)]
for node in nodes:
    print(node, '-', find_distance_between_nodes(tree, node))
