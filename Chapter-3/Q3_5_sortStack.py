class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size() - 1]

tempStack = Stack()
stack = Stack()


def sort():
    tempStack.push(stack.pop())
    while not stack.isEmpty():
        temp = stack.pop()
        while temp > tempStack.peek():
            stack.push(tempStack.pop())
        tempStack.push(temp)
    return tempStack

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

newStack = sort()

while newStack.size() != 0:
    print newStack.pop()
