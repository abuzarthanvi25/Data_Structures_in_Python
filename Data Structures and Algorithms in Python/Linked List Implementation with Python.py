# Q3. Linked List implementation
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

LL1=LinkedList()
LL1.add_begin(3318347850)
LL1.add_begin(3352251424)
LL1.add_begin(3425533201)
LL1.add_begin(3014765893)
LL1.print_LL()
