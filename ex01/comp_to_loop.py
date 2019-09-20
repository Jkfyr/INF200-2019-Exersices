def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    array = []
    for i in range(n):
        if i % 3 == 1:
            array.append(i**2)
    return array


if __name__ == '__main__':
    if squares_by_comp(2) != squares_by_loop(2):
        print('ERROR!')
