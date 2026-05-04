from DoublyLinkedList import DoublyLinkedList

DLL = DoublyLinkedList()

DLL.add_first(2)
DLL.add_first(3)
DLL.add_first(4)
print(DLL)
print(DLL.remove_between(DLL.header.next, DLL.trailer.prev))
print(DLL)
DLL.remove_last()
print(DLL)
print(DLL.size)