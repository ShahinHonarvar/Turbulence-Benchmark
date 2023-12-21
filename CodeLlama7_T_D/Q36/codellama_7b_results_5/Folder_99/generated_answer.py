
def filter_chars(my_string):
    filtered_string = ''
    for i in range(476, 948):
        if my_string[i] > 'b' and my_string[i] < 'd':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
