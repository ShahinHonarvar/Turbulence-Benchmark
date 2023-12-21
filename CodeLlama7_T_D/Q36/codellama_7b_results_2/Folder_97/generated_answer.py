
def filter_chars(my_string):
    filtered_string = ""
    for i in range(309, 591):
        if my_string[i] > 'S' and my_string[i] < 'm':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
