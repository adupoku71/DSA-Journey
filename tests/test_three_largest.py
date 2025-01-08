from Arrays.largest_three_distinct_in_array import find_three_largest_elements

def test_three_largest_1():
    assert find_three_largest_elements([12, 13, 1, 10, 34, 11, 34]) == [34, 13, 12]
    
    
def test_three_largest_2():
    assert find_three_largest_elements([10, 10, 10]) == [10]
    
    
def test_three_largest_3():
    assert find_three_largest_elements([10, 10, 9]) == [10, 9]
    

    
    