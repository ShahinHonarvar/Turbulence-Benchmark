
def filter_chars(my_string):
    filtered_string = ""
    for i in range(len(my_string)):
        if my_string[i] > 'h' and my_string[i] < 'k':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
