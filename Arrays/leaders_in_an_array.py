"""
Given an array of size n, Find all leaders in the array.
A leader is an element which is greater than or equal to
all the elements to its right side
Examples:
arr = [16, 17, 4, 3, 5, 2]
[17, 5, 2]
arr = [1, 2, 3, 4, 5, 2]
[5, 2]
"""

def leaders_in_array(arr):
    leaders = []
    n = len(arr)
    
    for x in range(n):
        isLeader = True
        for y in range(x + 1, n):
            if arr[x] < arr[y]:
                isLeader = False
                break
           
        if isLeader:
            leaders.append(arr[x])
    
    return leaders


def leaders_in_array_2(arr):
    n = len(arr)
    leaders = []
    for i in range(n):
        if max(arr[i:]) == arr[i]:
            leaders.append(arr[i])
    
    return leaders
    

def leaders_in_array_optimised(arr):
    leaders = []
    max_from_right = float('-inf')
    
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
            
    return leaders[::-1]

arr = [16, 17, 4, 3, 5, 2]
arr2 = [1, 2, 3, 4, 5, 2]
print(leaders_in_array_optimised(arr))