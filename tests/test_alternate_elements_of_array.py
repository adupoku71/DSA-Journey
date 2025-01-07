from Arrays.alternate_elements_of_array import find_alt_elements
# import Arrays
def test_alternate_elements_of_array1():
    assert find_alt_elements([10, 20, 30, 40, 50]) == [10, 30, 50]
    
def test_alternate_elements_of_array2():
    assert find_alt_elements([10, 20, 30, 40, 50, 60]) == [10, 30, 50]
    
def test_alternate_elements_of_array3():
    assert find_alt_elements([-5, 1, 4, 2, 12]) == [-5, 4, 12]