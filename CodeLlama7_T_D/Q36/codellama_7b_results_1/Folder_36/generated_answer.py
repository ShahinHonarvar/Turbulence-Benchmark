
def filter_chars(string):
    filtered_string = ""
    for i in range(283, 484):
        if string[i] > 'l' and string[i] < 't':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
