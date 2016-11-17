import sys

INT_MIN = -sys.maxint - 1
INT_MAX = sys.maxint

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBst(r):
    return (isBstUtil(r,INT_MIN, INT_MAX))

def isBstUtil(r, min_value, max_value):
    if r is None:
        return True

    if r.data < min_value or r.data > max_value:
        return False

    return (isBstUtil(r.left, min_value, r.data) and isBstUtil(r.right, r.data, max_value))


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBst(root)):
    print "Is BST"
else:
    print "Not a BST"


