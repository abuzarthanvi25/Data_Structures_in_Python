# Q3(d) Insertion in a sorted list

# Node Class
class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    # Function to initialize the head
    def __init__(self):
        self.head = None

    def sortedInsert(self, new_node):
        # For empty Linked List
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        # For head at end
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            # Locating the node before the point of insertion
            current = self.head
            while(current.next is not None and
                  current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node
    # function to insert a new node at the beggining
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = new_node
    # Utility function to print the linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
# Checking the program
Llist = Linked_List()
new_node = Node(3556556665)
Llist.sortedInsert(new_node)
new_node = Node(3216548484)
Llist.sortedInsert(new_node)
new_node = Node(3568715498)
Llist.sortedInsert(new_node)
new_node = Node(3457896512)
Llist.sortedInsert(new_node)
new_node = Node(3214578961)
Llist.sortedInsert(new_node)
new_node = Node(3215698747)
Llist.sortedInsert(new_node)

print("Create a Linked List")
Llist.print_list()
