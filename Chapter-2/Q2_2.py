from classes.LinkedList import *

linkedlist = randomLinkedList(10,3,7)
print linkedlist
head = linkedlist.head

def returnKthToLast(head, k):
    runner = head
    count = 1
    while runner.next != None:
        count += 1
        if count == k:
            current = head
        if count > k:
            current = current.next
        runner = runner.next
    return current

print returnKthToLast(head, 3)