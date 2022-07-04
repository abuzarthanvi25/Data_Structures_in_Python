# Q3(h) Deletion in a sorted list
# Main Class
class Sorted_Deletion:
    # Constructor
    def __init__(self):
        self.list=[]
    # Add function
    def add(self, item):
        self.list.append(item)
    # List sorting function
    def sort_list(self):
        self.list.sort()
        print(self.list)
    # function for deletion in list
    def deletion_in_list(self, del_item):
        if self.list != []:
            print(f"After deletion {del_item}")
            self.list.remove(del_item)
            print(self.list)

# Checking the program
obj = Sorted_Deletion()
obj.add("3245489525")
obj.add("3478964521")
obj.add("3145269853")
obj.add("3452786314")
obj.sort_list()
obj.deletion_in_list("3478964521")
