import pytest
from hw2_debugging import merge_sort, recombine

#Testing for an empty array
def test_merge_sort_empty_array():
    assert merge_sort([]) == []
