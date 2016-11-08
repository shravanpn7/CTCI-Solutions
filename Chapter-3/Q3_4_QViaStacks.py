from classes.Stack import Stack

newstack = Stack()
oldstack = Stack()

class QViaStacks():
    def __init__(self):
        print "init"

    def moveToOld(self):
        while not newstack.isEmpty():
            oldstack.push(newstack.pop())

    def enqueue(self,item):
        newstack.push(item)

    def dequeue(self):
        if oldstack.isEmpty():
            self.moveToOld()
        if not oldstack.isEmpty():
            return oldstack.pop()
        else:
            print "Queue empty"

    def isEmpty(self):
        return oldstack.isEmpty() and newstack.isEmpty()

    def size(self):
        return oldstack.size() + newstack.size()

q = QViaStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)


while not q.isEmpty():
    print q.dequeue()
