# Q3(e) Deletion of First Node
# Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Class of Linked List
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
    # Deleting the first node of the list
    def pop_front(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
    # Displaying the list
    def Print_List(self):
        temp = self.head
        if(temp != None):
            print("The List contains:", end=" ")
            while(temp!= None):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty now/n")
# Checking the program
MyLinkedList = Linked_List()
# Adding five elements in the list
MyLinkedList.push_end(3254567815)
MyLinkedList.push_end(3498656966)
MyLinkedList.push_end(3014578982)
MyLinkedList.push_end(3457215893)
MyLinkedList.push_end(3789612314)
MyLinkedList.Print_List()
# Deleting the first node
MyLinkedList.pop_front()
MyLinkedList.Print_List()
