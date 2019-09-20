def letter_freq(txt):
    letter_dict = {}

    txt = txt.lower()

    for n in txt:
        keys = letter_dict.keys()
        if n in keys:
            letter_dict[n] += 1
        else:
            letter_dict[n] = 1
    return letter_dict

    pass


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
