class Item:
    def __init__(self, k = None, v = None):
        self.key = k
        self.value = v

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

class ArrayMap:
    def __init__(self):
        # the map entries will be stored in a python list
        # which is implemented as a dynamic array
        self.the_table = []

    # return the number of entries in the map
    def get_size(self)->int:
        return len(self.the_table)

    # return a bool indicating whether or not M is empty
    def is_empty(self)->bool:
        return len(self.the_table) == 0

    # return the value associated with key k, if
    # it exists. Otherwise return None
    def get(self, k):
        # Traverse every item in the table
        for item in self.the_table:
            if item.key == k:
                return item.value
        # If we got this far, we didn't find it
        return None

    # If the map does not have an item associated with key k,
    # then create an item for k with value v and return None
    # Otherwise, replace the value associated with key k,
    # returning the old value
    def put(self, k, v):
        for item in self.the_table:
            if item.key == k:
                old_value = item.value
                item.value = v
                return old_value
        # If we got to here, it means we didn't find k in the map
        # So create a new item, append it to the list of entries, return None
        new_item = Item(k, v)
        self.the_table.append(new_item)
        return None

    # Remove the item with key k from the map, returning
    # the associated value. If there is no item with key k,
    # then return None
    def remove(self, k):
        for index, item in enumerate(self.the_table):
            if item.key == k:
                return_val = item.value
                self.the_table[index] = self.the_table[-1]
                self.the_table.pop()
                return return_val
        # if we got to here, the key k has no item in the table
        return None

    # Return an iterable containing all the keys stored in the map
    def keys(self):
        return [item.key for item in self.the_table]

    # Return an iterable containing all values stored in the map
    # There will be repetition if the same value appears twice
    def values(self):
        return [item.value for item in self.the_table]

    # Return an iterable containing all key-value entries in the map
    # Users of this method must import the class Item
    def entries(self):
        return [item for item in self.the_table]

    # Hmmm, is this the right thing to do?
    def __iter__(self):
        return self.keys()