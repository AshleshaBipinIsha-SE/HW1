import pytest
from hw2_debugging import merge_sort, recombine

#Testing for an empty array
def test_merge_sort_empty_array():
    assert merge_sort([]) == []

#Testing for an array with multiple elements
def test_merge_sort_manyelements():
    assert merge_sort([4, 1, 3, 4, 2, 4, 0, 9]) == [0, 1, 2, 3, 4, 4, 4, 9]
    

