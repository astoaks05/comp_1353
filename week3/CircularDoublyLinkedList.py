"""
Circular Doubly Linked List

Suggested instance attributes:
    self.cursor
    self.size
"""

class Node:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return self.__str__()
    
class CircularDoublyLinkedList:
    def __init__(self):
        self.cursor = None
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        if self.get_size() == 0:
            return True
        return False
    
    def __str__(self):
        if self.get_size() == 0:
            return '[]'
        return_str = '['
        temp = self.cursor
        while temp.next is not self.cursor:
            return_str += f'{temp.val}'
            temp = temp.next
        return_str += f'{temp.val}'
        return_str += ']'
        return return_str
    
    def add_after_cursor(self, v):
        if self.is_empty():
            new_node = Node(v)
            self.cursor = new_node
            self.cursor.next = new_node
            self.cursor.prev = new_node
            self.size += 1
        else:
            new_node = Node(v)
            new_node.next = self.cursor.next
            new_node.prev = self.cursor
            self.cursor.next = new_node
            new_node.next.prev = new_node
            self.size += 1
    
    def delete_cursor(self):
        if self.is_empty():
            raise IndexError('List is empty')
        elif self.get_size() == 1:
            return_val = self.get_value()
            self.cursor = None
            self.size -= 1
            return return_val
        return_val = self.get_value()
        self.cursor.prev.next = self.cursor.next
        self.cursor.next.prev = self.cursor.prev
        self.cursor = self.cursor.next
        self.size -= 1
        return return_val
    
    def advance_cursor(self, n):
        if self.is_empty():
            pass
        for i in range(n):
            self.cursor = self.cursor.next

    def get_value(self):
        if self.is_empty():
            raise IndexError('List is empty')
        return self.cursor.val


# import random
# import matplotlib.pyplot as plt
# import numpy as np 
# import time
# from week2.project1.DoublyLinkedList import DoublyLinkedList
# def homework_driver():
#     # X is the list of sizes of our data strcture
#     X = [5000 * i for i in range(1, 11)]

#     def create_double_linked_list(n):
#         trials = 50
#         new_list = DoublyLinkedList()
#         start = time.time()
#         for j in range(trials):
#             for i in range(n):
#                     new_list.insert(0, i)
#         end = time.time()
#         return ((end-start) / trials)

#     Y = [create_double_linked_list(x) for x in X]

#     plt.figure(figsize=(8, 5))
#     plt.plot(X, Y, marker='o', label='y label')
#     plt.title('Title of figure')
#     plt.xlabel('values added')
#     plt.ylabel('time')
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#     plt.savefig('example_figure.png')
# homework_driver()
