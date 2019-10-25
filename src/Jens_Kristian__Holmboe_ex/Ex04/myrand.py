# -*- coding: utf-8 -*-

__author__ = 'Jens Kristian Holmboe'
__email__ = 'Jholmboe@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7**5
        self.m = 2**31-1

    def rand(self):
        self.seed = self.a * self.seed % self.m

        return self.seed


class ListRand:
    def __init__(self, liste):
        self.list = liste
        self.list_len = len(liste)
        self.index = -1

    def rand(self):
        self.index += 1
        if self.index >= self.list_len:
            raise RuntimeError()
        return self.list[self.index]
