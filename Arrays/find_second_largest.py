"""
Find the second largest distinct element in an array of positive integers.
Return -1 if second largest element does not exit
"""

def find_second_largest(arr):
    largest = -1
    second_largest = -1
    
    for i in range(len(arr)):
        ele = arr[i]
        if ele > largest:
            second_largest = largest
            largest = ele
        elif ele > second_largest and ele < largest:
            second_largest = ele
    return second_largest

