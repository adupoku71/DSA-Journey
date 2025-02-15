def selection_sort(arr):
    
    length = len(arr)
    for i in range(length - 1):    
        smallest = i
        for j in range(i + 1, length):
            if arr[j] < arr[smallest]:
                smallest = j
                
        arr[i], arr[smallest] = arr[smallest], arr[i]
        
    return arr 