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


class Simulation:
    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        self.seed = seed
        self.x = 0

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walker = Walker(self.start, self.home)
        pos = walker.get_position()
        steps = walker.get_steps()
        while pos != self.home:
            walker.move()
            pos = walker.get_position()
            steps = walker.get_steps()
            # print(steps)
            # print("pos: {}".format(pos))
        return steps

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        walkers_steps = []
        random.seed(self.seed)
        for i in range(num_walks):
            walkers_steps.append(self.single_walk())
        return walkers_steps


if __name__ == "__main__":
    walk_sim_1 = Simulation(0, 10, 12345)
    walk_sim_2 = Simulation(10, 0, 12345)
    sim_walk_1 = Simulation(0, 10, 54321)
    sim_walk_2 = Simulation(10, 0, 54321)
    for i in range(2):
        print(walk_sim_1.run_simulation(20))
        print(walk_sim_2.run_simulation(20))
    print(sim_walk_1.run_simulation(20))
    print(sim_walk_2.run_simulation(20))

