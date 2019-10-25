# -*- coding: utf-8 -*-

__author__ = 'Jens Kristian Holmboe'
__email__ = 'Jholmboe@nmbu.no'


class Walker:
    def __init__(self, x0, home):
        self.home = home
        self.x0 = x0
        self.x = x0
        self.left = self.x - 1
        self.right = self.x + 1

    def move(self):
        if self.home > self.x0:
            self.x += 1
        elif self.home < self.x0:
            self.x -= 1
        else:
            pass
        return self.x

    def is_at_home(self):
        if self.x is self.home:
            return True
        return False

    def get_position(self):
        return self.x

    def get_steps(self):
        return self.x

