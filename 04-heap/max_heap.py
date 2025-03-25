
class MaxHeap:
    def __init__(self):
        self.data = [] 

    def add(self, value):
        self.data.append(value)
        self.heapify_up()

    def get(self):
        if self.is_empty():
            return None
        maximum = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop(-1)
        self.heapify_down()
        return maximum
    
    def heapify_down(self):
        pos = 0
        max_child = self.get_max_child_pos(pos)
        while max_child is not None:
            if self.data[pos] < self.data[max_child]:
                self.data[pos], self.data[max_child] = self.data[max_child], self.data[pos]
                pos = max_child
                max_child = self.get_max_child_pos(pos)
            else: 
                break

    def heapify_up(self):
        pos = len(self.data) - 1
        while pos > 0:
            parent = self.get_parent_pos(pos)
            if self.data[pos] > self.data[parent]:
                self.data[pos], self.data[parent] = self.data[parent], self.data[pos]
                pos = parent 
            else: 
                break

    def is_empty(self):
        return len(self.data) == 0

    def get_parent_pos(self, pos):
        return (pos - 1) // 2
    
    def get_left_child_pos(self, pos):
        p = 2 * pos + 1
        return p if p < len(self.data) else None
    
    def get_right_child_pos(self, pos):
        p = 2 * pos + 2
        return p if p < len(self.data) else None
    
    def get_max_child_pos(self, pos):
        left = self.get_left_child_pos(pos)
        right = self.get_right_child_pos(pos)
        if left is None and right is None:
            return None 
        elif right is None:
            return left 
        else:
            return left if self.data[left] > self.data[right] else right


heap = MaxHeap()
heap.add(7)
heap.add(12)
heap.add(34)
heap.add(9)
heap.add(18)
heap.add(42)

print(heap.data)

m = heap.get()
print(m)
print(heap.data)