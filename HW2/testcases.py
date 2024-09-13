"""importing merge sort module"""
from hw2_debugging import merge_sort

def test_merge_sort_empty_array():
    """Testing for an empty array"""
    assert merge_sort([]) == []

def test_merge_sort_manyelements():
    """Testing for an array with multiple elements"""
    assert merge_sort([4, 1, 3, 4, 2, 4, 0, 9]) == [0, 1, 2, 3, 4, 4, 4, 9]

def test_merge_sort_negatives():
    """Testing for negative elements"""
    assert merge_sort([-2, -2, -3, -1, -7, -8]) == [-8, -7, -3, -2, -2, -1]

def test_merge_sort_similars():
    """Testing for an array with all similar elements"""
    assert merge_sort([7, 7, 7]) == [7, 7, 7]
