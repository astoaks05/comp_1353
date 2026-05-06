from DoublyLinkedList import DoublyLinkedList as DLL

# right now I am building an abstract data type
class Queue: 
    def __init__(self):
        self.data = DLL()
    
    def enqueue(self, val):
        return self.data.add_last(val)
    
    def dequeue(self):
        return self.data.remove_first()
    
    def first(self):
        return self.data.first()

    def __len__(self):
        return self.data.get_size()
    
    def is_empty(self):
        return self.data.is_empty()
    
class Stack: 
    def __init__(self):
        self.data = DLL()
    
    def push(self, val):
        return self.data.add_first(val)
    
    def pop(self):
        return self.data.remove_first()
    
    def first(self):
        return self.data.first()
    
    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return self.data.get_size()

