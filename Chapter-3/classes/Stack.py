class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        length = self.size()
        i=0
        nodestore= []
        if length != 0:
            while i <= length:
                nodestore.append(str(self.pop()))
                return "Stack  [ " + "->".join(nodestore) + " ]"
        return "Stack  []"


