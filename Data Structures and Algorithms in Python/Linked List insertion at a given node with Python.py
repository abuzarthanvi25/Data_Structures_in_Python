# Q3(c) Insertion at given location
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    # Add new element ata the end of the list
    def push_end(self, newElement):
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
    # Method to insert a new element at a given position
    def push_at_position(self, newElement, position):
        newNode = Node(newElement)
        if(position < 1):
            print("\nposition should be >= 1")
        elif (position == 1):
                newNode.next = self.head
                self.head = newNode
        else:
            temp = self.head
            for i in range(1, position-1):
                if(temp != None):
                    temp = temp.next
            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode
            else:
                print("\nThe previous Node is Null")
    # Displaying the content of the list
    def Print_List(self):
        temp = self.head
        if(temp != None):
            print("The List contains:", end=" ")
            while (temp != None):
                print(temp.data, end = " ")
                temp = temp.next
            print()
        else:
            print("The list is empty")

# Checking the code
MyLinkedList = LinkedList()
# Adding three elements at the end of the list:
MyLinkedList.push_end(3318347850)
MyLinkedList.push_end(3352251424)
MyLinkedList.push_end(3568989578)
MyLinkedList.Print_List()
# Inserting an element at position 3
MyLinkedList.push_at_position(30125689589, 3)
MyLinkedList.Print_List()
# Inserting an element at position 1
MyLinkedList.push_at_position(3362562587, 1)
MyLinkedList.Print_List()

