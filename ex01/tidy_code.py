from random import randint as rnd

__author__ = 'Jens Kristain Holmboe'
__email__ = 'Jholmboe@nmbu.no'


def user_guess():
    guess_value = 0
    while guess_value < 1:
        guess_value = int(input('Your guess: '))
    return guess_value


def two_dice_rolls():
    return rnd(1, 6) + rnd(1, 6)


def check_value(sum_dices, your_guess):
    return sum_dices == your_guess


if __name__ == '__main__':

    win = False
    attempts = 3
    dice_value = two_dice_rolls()
    while not win and attempts > 0:
        user_value = user_guess()
        win = check_value(dice_value, user_value)
        if not win:
            print('Wrong, try again!')
            attempts -= 1

    if attempts > 0:
        print('You won {} points.'.format(attempts))
    else:
        print('You lost. Correct answer: {}.'.format(dice_value))
