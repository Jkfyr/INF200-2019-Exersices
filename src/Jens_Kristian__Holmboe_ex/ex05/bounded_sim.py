# -*- coding: utf-8 -*-

__author__ = 'Jens Kristian Holmboe'
__email__ = 'Jholmboe@nmbu.no'

from walker_sim import Walker, Simulation


# from myrand import LCGRand


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.x = start

    def lim_move(self):
        super().move()

        if self.x >= self.left_limit:
            self.x = self.left_limit
            self.step -= 1
        if self.x >= self.right_limit:
            self.x = self.right_limit


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def lim_move_sim(self):
        b_walker = BoundedWalker(self.start, self.home, self.left_limit,
                                 self.right_limit)
        while not b_walker.is_at_home():
            b_walker.lim_move()

        return b_walker.get_steps()


if __name__ == '__main__':
    for left_bound in [0, -10, -100, -1000, -10000]:
        steps = BoundedSimulation(0, 20, seed=12345,
                                  left_limit=left_bound,
                                  right_limit=20).run_simulation(20)
        print("left boundary: {:8d}: {}".format(left_bound, steps))
