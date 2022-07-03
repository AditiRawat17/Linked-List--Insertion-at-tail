# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
 
    print('None')
 
 
# Function to add a node at the tail end of the list instead of its head
def appendNode(head, key):
 
    current = head
    node = Node(key)
 
    # special case for length 0
    if current is None:
        head = node
 
    else:
        # locate the last node
        while current.next:
            current = current.next
        current.next = node
 
    return head
 
 
if __name__ == '__main__':
 
    # input keys
    keys = [1, 2, 3, 4]
 
    # points to the head node of the linked list
    head = None
    for key in keys:
        head = appendNode(head, key)
 
    # print linked list
    printList(head)
