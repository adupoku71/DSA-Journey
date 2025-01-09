from Arrays.check_if_array_is_sorted import check_if_sorted

def test_sorted_array_true():
    assert check_if_sorted([20, 21, 45, 89, 89, 90]) == True
    assert check_if_sorted([20, 20, 45, 89, 89, 90]) == True
    
    
def test_sorted_array_false():
    assert check_if_sorted([20, 20, 78, 98, 99, 97]) == False
    
    