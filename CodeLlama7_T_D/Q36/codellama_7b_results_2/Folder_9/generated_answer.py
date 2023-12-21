
def filter_chars(my_string):
    filtered_string = ""
    for i in range(50, 92):
        if my_string[i] > 'A' and my_string[i] < 'Q':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
