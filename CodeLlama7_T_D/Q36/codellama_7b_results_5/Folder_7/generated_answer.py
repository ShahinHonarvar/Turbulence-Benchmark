
def filter_chars(my_string):
    filtered_string = ""
    for i in range(502, 946):
        if my_string[i] > 'W' and my_string[i] < 'y':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
