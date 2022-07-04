# Q3(i) Searching in a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.last_node = None
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def find_index(self, key):
        current = self.head
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index = index + 1
        return -1
# Checking the program
a_Llist = Linked_List()
for data in [3256478125, 32579631450, 3562018967, 3452587523, 3416358206, 3145215412]:
    a_Llist.append(data)
print("The Linked List: ", end = " ")
a_Llist.display()
print()

key = int(input("What data item would you like to search for?: "))
index = a_Llist.find_index(key)
if index == -1:
          print(str(key) + "was not found")
else:
    print(str(key) + " is at index " + str(index) + ".")
