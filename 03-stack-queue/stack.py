
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            return None 
        else:
            value = self.data[-1]
            self.data.pop(-1)
            return value

    def is_empty(self):
        return len(self.data) == 0
    

stack = Stack()
stack.push(20)
stack.push(55)
stack.push(72)
v = stack.pop()
print(v)
stack.pop()
stack.pop()
v = stack.pop()
print(v)
