
class ListNode:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 



class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def is_empty(self):
        return self.head is None and self.tail is None 
    
    def add(self, value):
        node = ListNode(value)
        if self.is_empty():
            self.head = node 
            self.tail = node 
        else:
            node.next = self.head 
            self.head.prev = node 
            self.head = node 

    def display(self):
        iter = self.head 
        while iter is not None: 
            print(iter.value)
            iter = iter.next

    def remove(self, value):
        iter = self.head 
        while iter is not None:
            # Also check if:
            # - Remove the tail
            # - Remove the head 
            # - Remove the only one element in the list (head == tail)
            if iter.value == value:
                # - Some nod ein the middle of the list
                iter.next.prev = iter.prev 
                iter.prev.next = iter.next
                print("node deleted")
                return
            iter = iter.next
        print("node not found")

    


list = DoublyLinkedList()
print(list.is_empty())
list.add(38)
list.add(45)
list.add(11)
list.display()
print("Removing 45")
list.remove(45)
list.display()
list.remove(70)
print("Removing 38")
list.remove(38)