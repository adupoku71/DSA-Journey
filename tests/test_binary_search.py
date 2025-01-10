from Arrays.someArrayProblemTechniques.binary_search import binary_search, recursive_binary_search

arr1= [1, 2, 3, 4, 5, 6]
arr2 = [-5, -2, -1, 0, 1, 2, 3, 4, 5]
false_array = [78, -21, 45, 11, 45]

def test_bin_search():
  
    
    for i in arr1:
        assert binary_search(arr1, i) == True
        
    for i in arr2:
        assert binary_search(arr2, i) == True
        
    for i in false_array:
        assert binary_search(arr1, i) == False
        
    for i in false_array:
        assert binary_search(arr2, i) == False
        
        
        
def test_recursive_binary_search():
    for i in arr1:
        assert recursive_binary_search(arr1, 0, len(arr1) - 1, i) == True
        
    for i in arr2:
        assert recursive_binary_search(arr2, 0, len(arr2) - 1, i) == True
        
    for i in false_array:
        assert recursive_binary_search(arr1, 0, len(arr1) - 1, i) == False
        
    for i in false_array:
        assert recursive_binary_search(arr2, 0, len(arr2) - 1, i) == False
        