from Sorting_Algorithms.selection_sort import selection_sort

def test_selection_sort():
    arr1 = [4, 2, 1, 5, 3]
    arr2 = [-3, 7, -1, 0, 2, 5]

    assert selection_sort(arr1) == sorted(arr1)
    assert selection_sort(arr2) == sorted(arr2)