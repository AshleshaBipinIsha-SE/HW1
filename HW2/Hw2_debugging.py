"""
This module implements the merge sort algorithm and a helper function to merge two arrays.
It also integrates the use of the `rand` module to generate random arrays.
"""

import rand


def merge_sort(input_array):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        input_array (list): The list of numbers to sort.

    Returns:
        list: The sorted list.
    """
    if len(input_array) == 1:
        return input_array

    half = len(input_array) // 2

    return recombine(merge_sort(
        input_array[:half]), merge_sort(input_array[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left sorted array.
        right_arr (list): The right sorted array.

    Returns:
        list: The merged sorted array.
    """
    left_index = 0
    right_index = 0
    merged_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merged_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merged_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merged_arr[left_index + right_index] = left_arr[i]

    return merged_arr


# Renamed arr to random_array to avoid redefinition
random_array = rand.random_array([None] * 20)
sorted_array = merge_sort(random_array)

print(sorted_array)
