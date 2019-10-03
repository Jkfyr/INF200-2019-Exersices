def char_counts(textfilename: str) -> list:
    freq = [0]*256
    with open(textfilename, encoding='utf-8') as file:
        for line in file.readlines():
            for char in line:
                ascii_value = ord(char)
                freq[ascii_value] += 1
    return freq


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
