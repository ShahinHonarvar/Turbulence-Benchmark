
def filter_chars(my_string):
    filtered_string = ""
    for i in range(1, len(my_string)):
        if my_string[i] > '8' and my_string[i] < 'm':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
