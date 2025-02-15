from Arrays.remove_duplicates_from_sorted_array import remove_duplicates, remove_duplicates_optimised

def test_remove_duplicates():
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    
    assert remove_duplicates_optimised(arr) == len(set(arr))
    assert remove_duplicates(arr) == len(set(arr))
