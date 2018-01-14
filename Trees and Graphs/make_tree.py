# Without next pointer
class Tree:
    def __init__(self, data, left=None, right=None):
        self.node = data
        self.left = left
        self.right = right

# With next pointer
class Tree_Next:
    def __init__(self, data, left=None, right=None):
        self.node = data
        self.left = left
        self.right = right
        self.next = None

def get_tree(index=0):
    # Binary Search Tree (nodes = 7)
    if index == 0:
        '''
                4
            2       6
          1   3    5   7
        '''
        t1 = Tree(2, Tree(1), Tree(3))
        t2 = Tree(6, Tree(5), Tree(7))
        t = Tree(4, t1, t2)
        return t

    # Binary Tree (nodes = 10)
    elif index == 1:
        '''
                    1
                2       3
             4    5        6
               7         8
                9
                 10
        '''
        t1 = Tree(4, None, Tree(7, None, Tree(9, None, Tree(10))))
        t2 = Tree(2, t1, Tree(5))
        t3 = Tree(3, None, Tree(6, Tree(8)))
        t = Tree(1, t2, t3)
        return t

def get_tree_with_next(index=0):
    if index == 1:
        '''
                    1
                2       3
             4    5        6
               7         8
                9
                 10
        '''
        t1 = Tree_Next(4, None, Tree_Next(7, None, Tree_Next(9, None, Tree_Next(10))))
        t2 = Tree_Next(2, t1, Tree_Next(5))
        t3 = Tree_Next(3, None, Tree_Next(6, Tree_Next(8)))
        t = Tree_Next(1, t2, t3)
        return t

    elif index == 2:
        '''
                1
            2       3
          4   5    6   7
        '''
        t1 = Tree_Next(2, Tree_Next(4), Tree_Next(5))
        t2 = Tree_Next(3, Tree_Next(6), Tree_Next(7))
        t = Tree_Next(1, t1, t2)
        return t

    elif index == 3:
        '''
                1
                    3
                   6   7
        '''
        t2 = Tree_Next(3, Tree_Next(6), Tree_Next(7))
        t = Tree_Next(1, None, t2)
        return t

    else:
        '''
                4
            2       6
          1   3    5   7
        '''
        t1 = Tree_Next(2, Tree_Next(1), Tree_Next(3))
        t2 = Tree_Next(6, Tree_Next(5), Tree_Next(7))
        t = Tree_Next(4, t1, t2)
        return t
