""" 
Problem: Given an array arr[], the task is to print every
alternate element of the array starting from the first element.
Approach: Iterate through the array starting from index 0 and
increasing the index by 2 (index + 2) to move to the next alternate element
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_alt_elements(arr):
    alt_elements = []
    
    for i in range(0, len(arr), 2):
        alt_elements.append(arr[i])
        
    return alt_elements



if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    result = find_alt_elements(arr)
    print(" ".join(map(str, result)))
