# -*- coding: utf-8 -*-

__author__ = 'Jens Kristian Holmboe'
__email__ = 'Jholmboe@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))

# this code above is taken from this URL:
# https://github.com/yngvem/INF200-2019-Exercises/blob/master/exersices/ex03.rst


def test_one_element():
    data = [5]
    assert median(data) == 5


