from classes.LinkedList import *

linkedlist = randomLinkedList(4,3,7)
print linkedlist
head = linkedlist.head

data_list = []

def remove_dups(head):
    current = head
    while (current):
        if current.value not in data_list:
            data_list.append(current.value)
        else:
            prev.next = current.next
            current.next = None
        prev = current
        current = current.next

remove_dups(head)
print linkedlist