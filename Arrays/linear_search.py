"""
Problem: Given an array, arr of n integers, and an integer element x,
find whether element x is present in the array. Return the index of the
first occurrence of x in the array, or -1 if it doesn’t exist.
Input: arr[] = [1, 2, 3, 4], x = 3
Output: 2
Input: arr[] = [10, 8, 30], x = 6
Output: -1
"""

def linear_search(arr: list[int], x: int) -> int:
    
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    
    return -1


if __name__ == "__main__":
    print(linear_search([1, 2, 3, 4], 3))