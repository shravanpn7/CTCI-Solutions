class Tree:
    def __init__(self,rootObj):
        self.data = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = newNode
        else:
            t = Tree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = newNode
        else:
            t = Tree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.rightChild

    def setRootVal(self, data):
        self.data = data

    def getRootVal(self):
        return self.data
