"""
Starter code for a Singly Linked List homework assignment.

Required instance attributes:
    self.head
    self.size

Required methods:
    __init__(self)
    get_size(self)
    is_empty(self)
    __str__(self)
    add_first(self, value)
    add_last(self, value)
    remove_first(self)
    remove_last(self)
    get(self, index)
    remove_at_index(self, index)
"""


class Node:
    """A single node in a singly linked list."""

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class SinglyLinkedList:
    """A singly linked list that stores values in Node objects."""

    def __init__(self):
        """
        Create an empty singly linked list
        """
        self.head = None
        self.size = 0

    def __iter__(self):
        return SLLIterator(self.head)

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
        return (self.size == 0)

    def __str__(self):
        """
        Return a string showing all values in the list from first to last.

        Example format:
            [10 -> 20 -> 30]

        Returns:
            str: A string representation of the list contents.
        """
        curr = self.head
        string_result = '['
        while curr.next is not None:
            string_result += f'{curr.value}, '
            curr = curr.next
            

        string_result += f'{curr.value}'        
        string_result += ']'
        return string_result

    def add_first(self, value):
        """
        Insert a new node containing value at the front of the list.

        Args:
            value: The value to store in the new first node.

        Returns:
            None
        """
        new_node = Node(value, self.head)
        self.head = new_node
        self.size += 1

    def add_last(self, value):
        """
        Append a new node containing value to the end of the list.

        Args:
            value: The value to store in the new last node.

        Returns:
            None
        """
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        curr = self.head
        
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.size += 1

    def remove_first(self):
        """
        Remove the first node from the list and return its value.

        Returns:
            The value stored in the removed first node.

        Raises:
            IndexError: If the list is empty.
        """
        if not self.head:
            return IndexError
        return_val = self.head
        self.head = self.head.next
        self.size -= 1
        return return_val

    def remove_last(self):
        """
        Remove the last node from the list and return its value.

        Returns:
            The value stored in the removed last node.

        Raises:
            IndexError: If the list is empty.
        """
        if not self.head:
            return IndexError
        elif self.size == 1:
            return_val = self.head
            self.head = None
            return return_val
        curr = self.head
        while curr.next:
            curr = curr.next
        return_val = curr.next
        curr.next = None
        self.size -= 1
        return return_val

    def get(self, index):
        """
        Return the value stored at the given index.

        Args:
            index (int): The position to retrieve.

        Returns:
            The value stored at the given index.

        Raises:
            IndexError: If index is out of bounds.
        """
        if index < 0 or index > self.size - 1:
            return IndexError
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.value

    def remove_at_index(self, index):
        """
        Remove the node at the given index and return its value.

        Args:
            index (int): The position of the node to remove.

        Returns:
            The value stored in the removed node.

        Raises:
            IndexError: If index is out of bounds.
        """ 
        temp = self.head
        if index < 0 or index > self.size - 1:
            return IndexError
        if index == 0:
            self.remove_first()
        else:
            for i in range(index):
                temp = temp.next
            return_val = temp.next.value
            temp.next = temp.next.next
            return return_val
        self.size -= 1

    
    def min(self):
        temp = self.head
        min_val = temp.value

        while temp.next is not None:
            if temp.next.value < min_val:
                min_val = temp.next.value
            temp = temp.next
        return min_val

class SLLIterator:
    def __init__(self, head):
        self.cur = head
    
    def __next__(self):
        try:
            returnval = self.cur.value
            self.cur = self.cur.next
        except:
            raise StopIteration
        return returnval
    
    def __iter__(self):
        return self