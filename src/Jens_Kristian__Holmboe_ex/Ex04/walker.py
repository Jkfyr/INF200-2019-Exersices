# -*- coding: utf-8 -*-

__author__ = 'Jens Kristian Holmboe'
__email__ = 'Jholmboe@nmbu.no'

import random


class Walker:
    """
    class simulating movement of a person in a one dimensional world form A - B
    """
    def __init__(self, x0, home):
        """

        :param x0: start position
        :param home: home position
        """
        self.home = home
        self.x0 = x0
        self.x = x0
        self.step = 0

    def move(self):
        """
        if rnd gives you 0 you move to the left: x - 1
        if rnd gives you 1 you move to the right: x + 1
        :return: None
        """
        rnd = random.randint(0, 1)
        if rnd == 0:
            self.x -= 1
        else:
            self.x += 1
        self.step += 1

    def is_at_home(self):
        """
        :return: if you are home or not as True or False
        """
        if self.x is self.home:
            return True
        return False

    def get_position(self):
        """

        :return: x which is = to your position
        """
        return self.x

    def get_steps(self):
        """
        :return: step which is = how many steps you have taken so far
        """
        return self.step


def walk_home(x0, home):
    """
    :param x0: start position
    :param home: position of your home
    :return: Amount of steps you took from x0 to your home
    """
    walk = Walker(x0, home)
    pos = walk.get_position()
    steps = walk.get_steps()
    while pos != home:
        walk.move()
        pos = walk.get_position()
        steps = walk.get_steps()
    return steps


if __name__ == "__main__":
    distance = [1, 2, 5, 10, 20, 50, 100]
    tot_steps = [[] * i for i in range(len(distance))]
    for i, el in enumerate(distance):
        for k in range(0, 5):
            stp = walk_home(0, el)
            tot_steps[i].append(stp)
        print("Distance:   {0:4d}  -> Path lengths: {1} ".format(el,
                                                                 sorted(
                                                                     tot_steps[
                                                                         i])))
