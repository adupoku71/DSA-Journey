"""
Implementation of the selection sort algorithm
"""

def selection_sort(arr):
    n = len(arr)
    new_arr = arr[::]
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if new_arr[j] < new_arr[min_index]:
                min_index = j
        new_arr[i], new_arr[min_index] = new_arr[min_index], new_arr[i]
        
    return new_arr

        