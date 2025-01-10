def binary_search(arr, value):
    n = len(arr)
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        ele = arr[mid]
        
        if ele == value:
            return True
        if value > ele:
            left = mid + 1
        
        if value < ele:
            right = mid - 1
    return False
            
            
def recursive_binary_search(arr, left, right, value):
    if left > right:
        return False
    
    mid = (left +  right) // 2
    ele = arr[mid]
    
    if value == ele:
        return True
    if value > ele:
       return recursive_binary_search(arr, mid + 1, right, value)
    if value < ele:
       return recursive_binary_search(arr, left, mid - 1, value)
   
   
arr = [1, 2, 3, 4, 5, 6]

for i in arr:
    print(recursive_binary_search(arr, 0, len(arr) -1, i), end=" ")

print()
    
for i in arr:
    print(binary_search(arr, i), end=" ")
    
print()
print(recursive_binary_search(arr, 0, len(arr) - 1, 0))
print(binary_search(arr, -1))