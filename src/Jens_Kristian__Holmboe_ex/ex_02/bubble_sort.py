def bubble_sort(input_data):
    sorted_data = list(input_data)
    num_in_sorted_data = len(sorted_data)
    for index in range(num_in_sorted_data):
        for num in range(0, num_in_sorted_data - index - 1):
            if sorted_data[num] > sorted_data[num + 1]:
                sorted_data[num], sorted_data[num + 1] = sorted_data[num + 1], sorted_data[num]

    return sorted_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
