# -*- coding: utf-8 -*-

__author__ = 'Jens Kristian Holmboe'
__email__ = 'Jholmboe@nmbu.no'

import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    if n < 1:
        raise ValueError
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


# this code above is taken from this URL:
# https://github.com/yngvem/INF200-2019-Exercises/blob/master/exersices/ex03.rst


def test_one_element():
    data = [7]
    assert median(data) == 7


def test_odd_el():
    odd_data = [1, 3, 5, 7, 9]
    assert median(odd_data) == 5


def test_even_el():
    even_data = [4, 2, 8, 6, 10, 12]
    assert median(even_data) == 7


def test_ordered_el():
    data = [2, 5, 8, 4, 7, 9, 3]
    ordered_data = median(sorted(data))
    reversed_ord_data = median(list(reversed(data)))
    unordered_data = median(data)
    assert ordered_data == median(data)
    assert reversed_ord_data == median(data)
    assert unordered_data == median(data)


def test_empty_list():
    empty_list = []
    with pytest.raises(ValueError):
        median(empty_list)


def test_org_list():
    og_data = [3, 2, 1]
    data = og_data
    median(data)
    assert id(og_data) == id(data)


def test_tuple_list():
    tuple_data = (2, 3, 4, 9, 5)
    list_data = [2, 3, 4, 9, 5]
    median_tuple = median(tuple_data)
    median_data = median(list_data)
    assert median_tuple == median_data
