# Q3(g) Deletion of any given item of the node
# Node Class
class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_List:
    # Head initializer
    def __init__(self):
        self.head = None
    # Function for inserting new node in the begining
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    # Ref given for the head & key of list
    # Deleting the first occurance of key in linked list
    def deleteNode(self, key):
        # Storing head node
        temp = self.head
        # If head nodes contains deletion key
        if(temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        # Search for key to be deleted
        # Keeping track of the prev node
        # we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # if key was not present in the linked list
        if(temp == None):
            return
        # Unlinking the node from the linked list
        prev.next = temp.next
        temp = None
    # Printing the linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(" %d" %(temp.data)),
            temp = temp.next
# Checking the program
Llist = Linked_List()
Llist.push(3215257896)
Llist.push(3145269852)
Llist.push(3012045380)
Llist.push(3254775302)

print("Created Linked List: ")
Llist.print_list()
Llist.deleteNode(3145269852)
print("The Linked List after the Deletion of Node(3145269852) is: ")
Llist.print_list()
