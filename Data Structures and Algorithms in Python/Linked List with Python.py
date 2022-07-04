class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print("LINKED LIST IS EMPTY")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

LinkedL1=LinkedList()
LinkedL1.add_begin(3318347850)
LinkedL1.add_begin(3352251424)
LinkedL1.add_begin(3425533201)
LinkedL1.add_begin(3014765893)
LinkedL1.add_end(3045878903)
LinkedL1.add_end(3025632145)
LinkedL1.print_LL()
