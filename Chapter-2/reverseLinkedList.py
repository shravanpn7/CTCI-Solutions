from classes.LinkedList import *

linkedlist = randomLinkedList(4,3,7)
print linkedlist
head = linkedlist.head

def Reverse(head):
    current = head
    previous = None

    n = current.next

    while current is not None:
        # Reverse pointer to previous node
        current.next = previous

        # Prepare next node
        previous = current
        current = n

        try:
            n = n.next
        except Exception:
            return previous

new_head = Reverse(head)
while new_head != None:
    print new_head.value
    new_head = new_head.next