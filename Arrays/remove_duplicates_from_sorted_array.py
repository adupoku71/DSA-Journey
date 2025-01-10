"""
Given a sorted array, rearrange it such that all distinct
elements appear at the beginning in sorted order. Also return
the length of the distinct sorted subarray.
"""

def remove_duplicates(arr):
    
    hash_set = set()
    current_index = 0
    for i in range(len(arr)):
        if arr[i] not in hash_set:
            hash_set.add(arr[i])
            arr[current_index] = arr[i]
            
            current_index += 1
            
    return current_index


def remove_duplicates_optimised(arr):
    result = []
    seen = {}
    for num in arr:
        if num not in seen:
            result.append(num)
            seen[num] = True
    return len(result)
            
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
b = remove_duplicates_optimised(arr)
print(b)
print(arr)
        

        
