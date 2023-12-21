
def filter_chars(my_string):
    filtered_string = ""
    for i in range(1, len(my_string)):
        if my_string[i] > '-' and my_string[i] < 'L':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
