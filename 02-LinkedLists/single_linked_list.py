
class LisnkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LisnkedList:
    def __init__(self):
        self.head = None 

    def add(self, value):
        new_node = LisnkedListNode(value)
        new_node.next = self.head 
        self.head = new_node

    def display(self):
        iter = self.head 
        while iter is not None:
            print(iter.value)
            iter = iter.next
    
list = LisnkedList()
list.add(30)
list.add(36)
list.add(14)
list.display()



