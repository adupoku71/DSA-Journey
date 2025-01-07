from Arrays.linear_search import linear_search

def test_linear_search_1():
    assert linear_search([1, 2, 3, 4], 3) == 2
    
    
def test_linear_search_2():
    assert linear_search([10, 8, 30, 4, 5], 5) == 4
    

def test_linear_search_3():
    assert linear_search( [10, 8, 30], 6) == -1
    