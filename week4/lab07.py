
import numpy as np


#imagine that there is one big town that spans one very long road

# At the start is the Chamber of Commerce.

# This has addresses to some of the other areas of the town, including a residential neighborhood and apartment complexes. 

# The mayor of this town is also the postman and wants to deliver mail as efficiently as possible.

# The town has a few new residents move in 

#The town wants to alot some space for a large apartment complex so it finds a large piece of land and makes a 10 unit apartment. 

#Slowly, people move into the units of the apartment and move out. 

#When the 

class ArrayList:
    def __init__(self):
        self.capacity = 10  # initial capacity
        self.size = 0
        self.array = np.empty(self.capacity, dtype=object)

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        return self.array[i]

    def append(self, e):
        if self.size == self.capacity:
            self.expand_array()
        self.array[self.size] = e
        self.size += 1

    def remove(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        for j in range(i, self.size - 1):
            self.array[j] = self.array[j + 1]
        self.size -= 1

    def set(self, i, e):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        self.array[i] = e

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

class ArrayListGeometric(ArrayList):

    def expand_array(self):
        self.capacity *= 2
        new_array = np.empty(self.capacity, dtype=object)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __iter__(self):
        return ArrayListGeometricIterator(self)

class ArrayListArithmetic(ArrayList):

    def expand_array(self):
        self.capacity += 1000
        new_array = np.empty(self.capacity, dtype=object)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array 
        
class ArrayListGeometricIterator:
    def __init__(self, array_list):
        self.array_list = array_list
        self.index = 0

    def __next__(self):
        if self.index >= self.array_list.get_size():
            raise StopIteration
        value = self.array_list.get(self.index)
        self.index += 1
        return value
    
    def __iter__(self):
        return self 

test = ArrayListGeometric()
for i in range(1, 101):
    test.append(i)
total = 0
for num in test:
    total += num
print(total)