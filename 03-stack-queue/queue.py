
class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0
    
    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None 
        else: 
            value = self.data[0]
            self.data.pop(0)
            return value 
        

queue = Queue() 
queue.enqueue(19)
queue.enqueue(51)
queue.enqueue(28)
queue.enqueue(61)
v = queue.dequeue()
print(v)
queue.dequeue()
queue.dequeue()
queue.dequeue()
v = queue.dequeue()
print(v)