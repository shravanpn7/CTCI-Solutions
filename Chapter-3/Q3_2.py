class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)
        if len(self.minstack) == 0 or item <= self.minstack[-1]:
            self.minstack.append(item)

    def pop(self):
        if self.peek() == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def min(self):
        return self.minstack[-1]

stack = MinStack()
stack.push(-1)
stack.push(3)
stack.push(-12)
stack.push(-11)
stack.push(13)


print stack.min()


