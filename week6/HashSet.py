"""
Code for the implementation of the HashSet abstract data type. Written by Aidan Stoaks May 9th, 2026 for the DU COMP1353 class, for the Homework 11-12 assignment.
"""
import numpy as np
from random import choice, randint, random

class HashSet:
    """
    A hashmap that stores values in python sets
    """
    PRIMES = (25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741)

    def __init__(self):
        """
        Create an empty HashSet
        """
        self._init_table(16)

    def _init_table(self, new_capacity):
        """
        Inititalizes the HashSet, taking an integer new_capacity as a parameter for the number of buckets

        Args:
            new_capacity: the new size of the table to be initialized

        Returns: 
            None
        """
        self.the_table = np.empty(new_capacity, dtype=set)
        self.prime = choice(HashSet.PRIMES)
        self.a = randint(1, self.prime-1)
        self.b = randint(0, self.prime-1)
        self.size = 0

        #create all the buckets
        for i in range(len(self.the_table)):
            self.the_table[i] = set()

    def _hash_and_compress(self, k):
        """
        Produces an index based on the element of the set

        Args:
            k: the value to be hashed

        Returns:
            The hash index in the table where the value will be stored
        """
        return (hash(k) * self.a + self.b) % self.prime % len(self.the_table)

    def _expand_table(self):
        """
        Initializes a new table containing all old values, but with a larger capacity (twice as much as before)
        """
        old_items = list(self.items())
        self._init_table(len(self.the_table)*2)
        for item in old_items:
            index = self._hash_and_compress(item)
            self.the_table[index].add(item)
            self.size += 1

    def get_size(self):
        """
        Return the amount of items inside a HashSet

        Returns:
            Number of items stored in a HashSet
        """
        return self.size

    def add(self, v):
        """
        Adds a value to a set stored inside a HashSet

        Args:
            v: the value to be added to a set stored in the HashSet object

        Returns:
            None
        """
        index = self._hash_and_compress(v)
        bucket = self.the_table[index]
        old_len = len(bucket)
        bucket.add(v)
        if len(bucket) > old_len:  # Item was actually added
            self.size += 1
        # check if we must expand the table
        load_factor = self.size / len(self.the_table)
        if load_factor > 0.75:
            self._expand_table()
    
    def discard(self, v):
        """
        Removes a value if it exists in the HashSet, does nothing otherwise

        Args:
            v: the value to be removed, given that it exists in the HashSet object

        Returns: 
            None
        """
        index = self._hash_and_compress(v)
        bucket = self.the_table[index]
        if v in bucket:
            bucket.remove(v)
            self.size -= 1

    def contains(self, v):
        """
        Checks to see if a value exists within a HashSet

        Args:
            v: the value to be checked for existnce within the HashSet object

        Returns:
            bool: True if the value is found, False otherwise
        """
        index = self._hash_and_compress(v)
        return v in self.the_table[index]
    
    def union(self, other):
        """
        Creates a new HashSet with all the values of both HashSets being compared

        Args:
            other: a HashSet of which all of its values will be added to the values of self into a new HashSet object

        Returns:
            res: a new HashSet containing all values of both arguments
        """
        res = HashSet()
        for item in self.items():
            res.add(item)
        for item in other.items():
            res.add(item)
        return res
    
    def intersection(self, other):
        """
        Creates a new HashSet containing only elements that are shared between two other HashSets

        Args: 
            other: a HashSet being compared to self

        Returns:
            A new HashSet object, which only contains values shared between both arguments
        """
        res = HashSet()
        for item in self.items():
            if other.contains(item):
                res.add(item)
        return res
    
    def difference(self, other):
        """
        Creates a new HashSet which contains only items stored in self, that are different from the compared HashSet

        Args:
            other: the HashSet object being compared to self

        Returns:
            A new HashSet object which contains only items in self that were not found in the other HashSet
        """
        res = HashSet()
        for item in self.items():
            if not other.contains(item):
                res.add(item)
        return res

    def __str__(self):
        """
        Returns a string representation of a HashSet object

        Returns:
            A string representation of a HashSet object
        """
        res = ''
        for bucket in self.the_table:
            if len(bucket) == 0:
                res += ('[]\n')
            else:
                for item in bucket:
                    res += f'{item}, '
                res += '\n'
        return res
    
    # iterables
    def items(self):
        """
        Returns every item in the HashSet
        """
        return (item for bucket in self.the_table for item in bucket)
    
    def __iter__(self):
        """
        Returns self.items()
        """
        return self.items()

def main():
    female_names = HashSet()
    male_names = HashSet()
    with open('femaleNames2016.txt', 'r') as females:
        for line in females:
            parts = line.split()
            female_names.add(parts[0])
    with open('maleNames2016.txt', 'r') as males:
        for line in males:
            parts = line.split()
            male_names.add(parts[0])
    intersection = female_names.intersection(male_names)
    print(f'Number of intersected names: {intersection.get_size()}')
    print(f'List of intersected names: {list(intersection)}')

if __name__ == '__main__':
    main()



