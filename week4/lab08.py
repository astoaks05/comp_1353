from SinglyLinkedList import SinglyLinkedList as SLL
from DoublyLinkedList import DoublyLinkedList as DLL

Listy = SLL()
Listy.add_first(1)
Listy.add_first(2)
Listy.add_first(3)

Listy2 = DLL()
Listy2.add_first(1)
Listy2.add_first(2)
Listy2.add_first(3)


# for num in Listy:
#     print(num)

for num in Listy2:
    print(num)





# import time

# # iterators
# stream1 = [1, 3, 5, 7, 9]
# stream2 = [2, 4, 6, 8, 10]

# # stream3 = []

# # while stream1:
# #     stream3.append((stream1.pop(0), stream2.pop(0)))
# #     time.sleep(3)

# # print(stream3)
# # a = [1, 3, 5, 7]
# # b = [2, 4, 6, 8]
# # c = zip(a, b)

# # print(list(c))

# nums = [10, 20, 30]

# it1 = iter(nums)
# it2 = iter(nums)

# print(next(it1))
# print(next(it2))

# print(next(it1))
# print(next(it1))

# # iter method for a SLL 
# def __iter__(self):
#     '''
#     yield values from head to tail so SLL is iterable.
#     '''
#     cur = self.head
#     while cur:
#         yield cur.value # kind of like return, but we do not stop the loop
#         cur = cur.next



