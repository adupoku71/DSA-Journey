from Arrays.leaders_in_an_array import leaders_in_array_optimised

def test_leaders():
    arr = [16, 17, 4, 3, 5, 2]
    arr2 = [1, 2, 3, 4, 5, 2]
    
    assert leaders_in_array_optimised(arr) == [17, 5, 2]
    assert leaders_in_array_optimised(arr2) == [5, 2]

