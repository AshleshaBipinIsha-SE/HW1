import pytest
from hw2_debugging import merge_sort, recombine

#Testing for an empty array
def test_merge_sort_empty_array():
    assert merge_sort([]) == []

#Testing for an array with multiple elements
def test_merge_sort_manyelements():
    assert merge_sort([4, 1, 3, 4, 2, 4, 0, 9]) == [0, 1, 2, 3, 4, 4, 4, 9]

#Testing for negative elements 
def test_merge_sort_negatives(): 
    assert merge_sort([-2, -2, -3, -1, -7, -8]) == [-8, -7, -3, -2, -2, -1]

#Testing for an array with all similar elements
def test_merge_sort_similars():
    assert merge_sort([7, 7, 7]) == [7, 7, 7]


    

