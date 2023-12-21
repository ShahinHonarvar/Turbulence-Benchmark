
def filter_chars(my_string):
    filtered_string = ""
    for i in range(3, 8):
        if my_string[i] > '?' and my_string[i] < 'k':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
