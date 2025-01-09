"""
Given an array, check if it is sorted in ascending order
"""

def check_if_sorted(arr):
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True
    
    