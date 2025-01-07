"""
Given an array arr. The task is to find the largest element in the given array. 

Examples: 

Input: arr[] = [10, 20, 4]
Output: 20
Input: arr[] = [20, 10, 20, 4, 100]
Output: 100

"""

def find_largest(arr):
    largest = arr[0]
    
    for ele in arr:
        if ele > largest:
            largest = ele
    
    return largest
    
