# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
class SinglyLinkedList:
    def __init__ (self):
        self.head = None

def printLinkedList(head):
    itr = head
    while itr:
        print(itr.data)
        itr = itr.next 
    
if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
