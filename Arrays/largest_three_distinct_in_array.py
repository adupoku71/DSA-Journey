"""
Find the three largest disntict elements in an array of integers
"""

def find_three_largest_elements(arr):
    if len(arr) < 3:
        return None
    
    first = second = third = float('-inf')
    
    for i in range(len(arr)):
        ele = arr[i]
        if ele > first:
            third = second
            second = first
            first = ele
        elif ele > second and ele < first:
            third = second
            second = ele
        elif ele > third and ele < second:
            third = ele
    print(first, second, third)       
    return [x for x in [first, second, third] if x > 0]

arr = [10, 10, 10]
[12, 13, 1, 10, 34, 11, 34]
print(find_three_largest_elements(arr))
