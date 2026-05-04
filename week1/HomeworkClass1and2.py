from SinglyLinkedList import SinglyLinkedList
import random
"""
Homework placeholder for class assignments 1 and 2.

Use this file for homework driver code, assignment examples, or small
tests related to linked list work from the first two class homework sets.
"""



def homework_driver():
    random.seed(1)
    testing_list= SinglyLinkedList()
    for i in range(1,4):
        testing_list.add_first(i * random.randint(0,10))
        testing_list.add_last(i * random.randint(0,10))
        testing_list.add_first(i * random.randint(0,10))
        testing_list.add_last(i * random.randint(0,10))
    # print(TestingList)
    for _ in range(5):
        rand_index=random.randint(0,20)
        # print(f'rand_index is {rand_index}')
        try: testing_list.remove_at_index(rand_index)
        except IndexError as e:
            pass
            # print(e)
    print(testing_list)

#The following is the main code block:
homework_driver()


