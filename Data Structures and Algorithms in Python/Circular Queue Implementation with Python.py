# Q.2 ( CIRCULAR QUEUE IMPLEMENTATION IN PYTHON )
class Circular_Queue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Inserting an element into our circular queue
    def queue_insert(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is now full\n\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Deleting an element from our circular queue
    def queue_delete(self):
        if (self.head == -1):
            print("The circular queue is now empty\n\n")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def queue_print(self):
        if self.head == -1:
            print("There is no element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end = " ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
# The Circular_Queue object will be initiated and called by the following methods:
obj = Circular_Queue(6)
obj.queue_insert(1)
obj.queue_insert(2)
obj.queue_insert(3)
obj.queue_insert(4)
obj.queue_insert(5)
obj.queue_insert(6)
print("The Initial Queue (Before any operations performed)")
obj.queue_print()

obj.queue_delete()
print("The queue after removing an element from itelf")
obj.queue_print()
