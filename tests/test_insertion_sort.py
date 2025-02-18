from Sorting_Algorithms.insertion_sort import insertion_sort

def test_insertion_sort():
    arr1 = [4, 2, 1, 5, 3]
    arr2 = [-3, 7, -1, 0, 2, 5]

    assert insertion_sort(arr1) == sorted(arr1)
    assert insertion_sort(arr2) == sorted(arr2)