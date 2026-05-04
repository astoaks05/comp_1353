"""
Filename: algo_analysis.py
Author: Stoaks
Description: A file containing functions with three different algorithms, and functions that calculate the average runtime of each of these algorithms
Collaborators: DU Comp Sci Dept.
Assigment: Project 2: Algorithm Analysis
Date: 4-23-2026
"""

import random
import time

def sequential(l: list):
    """
    Perform a sequential search on a list of integers

    Args:
        l: list
    
    Returns:
        Boolean
    """
    if len(l) == 0:
        raise ValueError('list is empty')
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j] * -1:
                return True
    return False

def time_sequential(num_trials: int, list_size: int, test_list: list):
    """
    Calculate the average runtime of a sequential search given a number of trials and list size

    Args:
        num_trials: int
        list_size: int
        test_list: list
    
    Returns:
        average_runtime: str
    """
    total_time = 0
    for i in range(num_trials):
        start = time.time()
        sequential(test_list)
        end = time.time()
        total_time += end-start
    return f'The average time to perform sequential search on a list with {list_size} values is {(total_time/num_trials):.5f} seconds, using {num_trials} trials'

def binary(start: int, end: int, target: int, l: list):
    """
    Complete a binary search given a start, an end, a target, and a list

    Args:
        start: int
        end: int
        target: int
        l: list
    
    Returns:
        Boolean
    """
    if start > end:
        return False
    mid = (start+end) // 2
    if l[mid] == target:
        return True
    elif target < l[mid]:
        end = mid-1
    elif target > l[mid]:
        start = mid+1
    return binary(start, end, target, l)

def time_binary(num_trials: int, list_size: int, test_list: list):
    """
    Calculate the average runtime for the binary search function given a number of trials and the size of the list

    Args:
        num_trials: int
        list_size: int
        test_list: list
    
    Returns: 
        average_runtime: str
    """
    total_time = 0
    for i in range(num_trials):
        start = time.time()
        results = [binary(0, len(test_list)-1, num*(-1), test_list) for num in test_list]
        end = time.time()
        total_time += end-start
    return f'The average time to perform binary search on a list with {list_size} values is {(total_time/num_trials):.5f} seconds, using {num_trials} trials'

def two_indices(l:list):
    """
    Keep two indices that move towards eachother searching for its opposite

    Args:
        l: list
    
    Returns: 
        Boolean
    """
    i = 0
    j = len(l)-1
    while l[i]+l[j] != 0:
        if l[i] + l[j] < 0:
            i+=1
        elif l[i] + l[j] > 0:
            j-=1
        if j == i:
            return False
    return True

def time_two_indices(num_trials: int, list_size: int, test_list: list):
    """
    Calculate the average run time of the two_indices search with varying numbers of trials and sizes of lists

    Args:
        num_trials: int
        list_size: int
        test_list: list

    Returns:
        average_runtime: string
    """
    total_time = 0
    for i in range(num_trials):
        start = time.time()
        two_indices(test_list)
        end = time.time()
        total_time += end-start
    return f'The average time to perform two_indices search on a list with {list_size} values is {(total_time/num_trials):.5f} seconds, using {num_trials} trials' 

def main():
    n = 80000 # number of values
    # test list contains ONLY positives, to ensure worst case happens every time
    test_list = sorted([random.randint(1, 5000) for _ in range(n)])
    print(time_sequential(1, n, test_list))
    print(time_binary(50, n, test_list))
    print(time_two_indices(50, n, test_list))


if __name__ == '__main__':
    main()