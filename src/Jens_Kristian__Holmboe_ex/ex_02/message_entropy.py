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


def entropy(message):
    import math
    freq = letter_freq(message)
    teller = len(message)
    array = []
    for i in freq.keys():
        p_entropy = -(freq[i]/teller * (math.log2(freq[i]/teller)))
        array.append(p_entropy)
    entropy_val = sum(array)
    return entropy_val


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
