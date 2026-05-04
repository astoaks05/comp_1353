"""
Starter code for Doubly Linked List lab and homework work.

Suggested instance attributes:
    self.head
    self.tail
    self.size

This starter includes a common set of list methods so students can fill
in the implementation details later. The __str__ method is intended as a
lab task, and search(val) is included as a later method that returns
the index of the first matching val or -1 if not found.
"""


class Node:
    """A single node in a doubly linked list."""

    def __init__(self, val,  prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


class DoublyLinkedList:
    """A doubly linked list that stores values in Node objects."""

    def __init__(self):
        """
        Create an empty doubly linked list.

        TODO:
        - Set head to None.
        - Set tail to None.
        - Set size to 0.
        """
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __iter__(self):
        return DLLIterator(self.header)

    def get_size(self):
        """
        Return the number of nodes currently in the list.

        Returns:
            int: The current size of the list.
        """
        return self.size

    def is_empty(self):
        """
        Return True if the list has no nodes, otherwise return False.

        Returns:
            bool: True when the list is empty, False otherwise.
        """
        return self.size == 0

    def __str__(self):
        """
        LAB TASK:
        Implement __str__ for the DoublyLinkedList class.

        Return a string showing all values in the list from first to last.

        Example format:
            [2, 4, 6]

        Returns:
            str: A string representation of the list contents.
        """
        string_rep = '['
        cur = self.header.next
        while cur is not self.trailer:
            string_rep += f'{cur.val}'
            if cur.next is not self.trailer:
                string_rep += ', '
            cur = cur.next
        string_rep += ']'
        
        return string_rep

    def add_first(self, val):
        """
        Insert a new node containing val at the front of the list.

        Args:
            val: The val to store in the new first node.

        Returns:
            None
        """
        temp = Node(val, self.header, self.header.next)
        temp.prev.next = temp
        temp.next.prev = temp
        self.size += 1

    def add_last(self, val):
        """
        Append a new node containing val to the end of the list.

        Args:
            val: The val to store in the new last node.

        Returns:
            None
        """
        new_node = Node(val, self.trailer.prev, self.trailer)
        if self.get_size() == 0:
            self.header.next = new_node
            self.trailer.prev = new_node
        self.trailer.prev.next = new_node
        self.trailer.prev = new_node
        self.size += 1

    def remove_first(self):
        """
        LAB TASK:
        Implement remove_first for the DoublyLinkedList class.

        Remove the first node from the list and return its val.

        Returns:
            The val stored in the removed first node.

        Raises:
            IndexError: If the list is empty.
        """
        return self.remove_between(self.header, self.header.next.next)

    def remove_last(self):
        """
        LAB TASK:
        Implement remove_last for the DoublyLinkedList class.

        Remove the last node from the list and return its val.

        Returns:
            The val stored in the removed last node.

        Raises:
            IndexError: If the list is empty.
        """
        return self.remove_between(self.trailer.prev.prev, self.trailer)
    
    def first(self):
        if self.get_size() != 0:
            return self.header.next.val
        raise IndexError('List is empty')

    def last(self):
        if self.get_size() != 0:
            return self.trailer.prev.val
        raise IndexError('List is empty')

    def remove_between(self, node1, node2):
        # check if either node is None
        if node1 is None or node2 is None:
            raise IndexError('One or both nodes are None')
        # check to make sure the nodes are only one node apart
        if not (node1.next.next == node2):
            raise ValueError('Nodes are more than one node apart')
        return_val = node1.next.val
        node1.next = node2
        node2.prev = node1
        self.size -= 1
        return return_val

    def get(self, index: int):
        """
        Return the val stored at the given index.

        Args:
            index (int): The position to retrieve.

        Returns:
            The val stored at the given index.

        Raises:
            IndexError: If index is out of bounds.
        """
        if index < 0 or index > self.get_size() - 1:
            raise IndexError('Index out of range, size of list')
        cur = self.header.next
        for i in range(index):
            cur = cur.next

        return cur.val

    def remove_at_index(self, index: int):
        """
        Remove the node at the given index and return its val.

        Args:
            index (int): The position of the node to remove.

        Returns:
            The val stored in the removed node.

        Raises:
            IndexError: If index is out of bounds.
        """
        if index < 0 or index > self.size - 1:
            raise IndexError('Index out of range')
        if index == self.size - 1:
            self.remove_last()
        elif index == 0:
            self.remove_first()
        else:
            cur = self.header.next # cur is the first element in the list
            for i in range(index):
                cur = cur.next
            return_val = cur.val
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            self.size -= 1
            return return_val

    def search(self, val):
        """
        Return the index of the first occurrence of val in the list.

        Args:
            val: The val to search for.

        Returns:
            int: The index of the first matching node, or -1 if the val
            does not appear in the list.
        """
        index = -1
        cur = self.header
        while cur.next is not None:
            if cur.val == val:
                return index
            index += 1
            cur = cur.next
        return -1
    

class DLLIterator:
    def __init__(self, header):
        self.cur = header.next

    def __next__(self):
        if self.cur.val is None:
            raise StopIteration
        try:
            returnval = self.cur.val
            self.cur = self.cur.next
        except:
            raise StopIteration
        return returnval
    
    def __prev__(self):
        try:
            returnval = self.cur.prev.val
            self.cur.prev = self.cur
        except:
            raise StopIteration
        return returnval
    
    def __iter__(self):
        return self

# def testing():
#     DLL = DoublyLinkedList()
#     DLL.add_first(3)
#     DLL.add_first(2)
#     DLL.add_first(1)
#     DLL.add_last(4)
#     DLL.add_last(5)
#     print(DLL)
#     print(DLL.get(1))
#     print(DLL)
#     DLL.remove_at_index(4)
#     print(DLL)
#     print(DLL.search(12))

# def dll_tester():
#     # create a DoublyLinkedList
#     test_list = DoublyLinkedList()
    
#     #testing list creation
#     assert test_list.get_size()==0,   'list should be empty to start!'
    
#     #testing add_first
#     test_list.add_first(1)
#     assert test_list.first() == 1, 'add_first needs adjustment!'
#     assert test_list.last() == 1, 'add_first needs adjustment!'
#     assert test_list.get_size() == 1 ,    'add_first needs adjustment!'
#     test_list.add_first(2)
#     assert test_list.first() == 2, 'add_first needs adjustment!'
#     assert test_list.last() == 1, 'add_first needs adjustment!'
#     assert test_list.get_size() == 2, 'add_first needs adjustment!'
    
#     #testing add_last
#     test_list.add_last(3)
#     assert test_list.first() == 2,'add_last needs adjustment!'
#     assert test_list.last() == 3, 'add_last needs adjustment!'
#     assert test_list.get_size() == 3, 'add_last needs adjustment!'

#     #test remove_first
#     assert test_list.remove_first() == 2, 'remove_first needs adjustment!'
#     assert test_list.first() == 1, 'remove_first needs adjustment!'
#     assert test_list.last() == 3, 'remove_first needs adjustment!'
#     assert test_list.get_size() == 2, 'remove_first needs adjustment!'

#     #test remove_last
#     assert test_list.remove_last() == 3, 'remove_last needs adjustment!'
#     assert test_list.first() == 1, 'remove_last needs adjustment!'
#     assert test_list.last() == 1, 'remove_last needs adjustment!'
#     assert test_list.get_size() == 1, 'remove_last needs adjustment!'

#     while not test_list.is_empty():
#         test_list.remove_first()

#     assert test_list.get_size() == 0, 'list should be empty after removing all values'    

#     for i in range(10):
#         test_list.add_last(i+1)
#     #test get method
#     assert test_list.get(0) == 1, 'get(0) should return the element at first index'
#     assert test_list.get(5) == 6, 'get(1) should return the element at index 1'
#     assert test_list.get(9) == 10, 'get(9) should return the element at last index'

#     print('All tests passed!')
# # dll_tester()