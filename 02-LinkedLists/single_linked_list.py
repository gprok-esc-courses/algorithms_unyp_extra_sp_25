
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None 


class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def add(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        iterator = self.head
        while iterator is not None:
            print(iterator.value)
            iterator = iterator.next

    def remove(self, value): 
        iterator = self.head
        previous_iterator = None 
        while iterator is not None:
            if iterator.value == value:
                if previous_iterator is None:    # it's the first node
                    self.head = iterator.next
                else:
                    previous_iterator.next = iterator.next 
                return True
            previous_iterator = iterator
            iterator = iterator.next
        return False




data = SinglyLinkedList() 
data.add(35)
data.add(56)
data.add(10)
data.add(21)
data.add(67)
data.display()
print("REMOVE 10")
data.remove(10)
data.display()
print("REMOVE 35 - LAST ONE")
data.remove(35)
data.display()
print("REMOVE 67 - FIRST ONE")
data.remove(67)
data.display()
