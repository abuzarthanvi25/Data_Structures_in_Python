# Q3(f) Deletion of the last node
# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Linked List class
class Linked_List:
    def __init__(self):
        self.head = None
    # Adding new element to the end of the list
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
    # Deleting the last node of the list
    def pop_end(self):
        if(self.head != None):
            if(self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                lastNode = None
    # Displaying the linked list
    def print_list(self):
        temp = self.head
        if(temp != None):
            print("The list contains:", end=" ")
            while (temp != None):
                print(temp.data, end= " ")
                temp = temp.next
            print()
        else:
            print("The List is empty now")
# Checking the program
My_Linked_List = Linked_List()
# Adding four elements into the list
My_Linked_List.push_end(3214568795)
My_Linked_List.push_end(3245789632)
My_Linked_List.push_end(3457856123)
My_Linked_List.push_end(3145389276)
My_Linked_List.print_list()
# Deleting the last Node
My_Linked_List.pop_end()
My_Linked_List.print_list()
