# -*- coding: utf-8 -*-

__author__ = 'Jens Kristian Holmboe'
__email__ = 'Jholmboe@nmbu.no'
import pytest
from collections import Counter


def bubble_sort(input_data):
    sorted_data = list(input_data)
    num_in_sorted_data = len(sorted_data)
    for index in range(num_in_sorted_data):
        for num in range(0, num_in_sorted_data - index - 1):
            if sorted_data[num] > sorted_data[num + 1]:
                sorted_data[num], sorted_data[num + 1] = sorted_data[num + 1], sorted_data[num]

    return sorted_data


def test_empty():
    """Test that the sorting function works for empty list"""
    liste = []
    assert (bubble_sort(liste)) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    list_single = len([1])
    assert len(bubble_sort([3])) == list_single


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    test = data is sorted_data
    if test is False:
        assert True
    else:
        assert False


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert Counter(data) == Counter(sorted_data)


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(sorted(data))
    bubble_data = bubble_sort(data)
    assert sorted_data == bubble_data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    reversed_data = list(reversed(data))
    sorted_rev = bubble_sort(reversed_data)
    assert sorted_rev == sorted_data


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass
