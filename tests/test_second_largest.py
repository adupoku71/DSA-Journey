from Arrays.find_second_largest import find_second_largest


def test_find_second_largest_1():
    arr = [1, 2, 3, 4, 5, 6]
    assert find_second_largest(arr) == 5
    
    
def test_find_second_largest_2():
    arr = [1, 2, 3, 4, 5, 5, 6]
    assert find_second_largest(arr) == 5
    
    
def test_find_second_largest_3():
    arr = [7, 4, 10, 4, 5, 6]
    assert find_second_largest(arr) == 7
    
    
def test_find_second_largest_4():
    arr = [20, 10, 20, 4, 100]
    assert find_second_largest(arr) == 20
    
    
def test_find_second_largest_5():
    arr = []
    assert find_second_largest(arr) == -1
    

def test_find_second_largest_6():
    arr = [8]
    assert find_second_largest(arr) == -1
    

def test_find_second_largest_7():
    arr = [8, 2]
    assert find_second_largest(arr) == 2