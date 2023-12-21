
def filter_chars(my_string):
    filtered_string = ""
    for i in range(len(my_string)):
        if my_string[i] >= '7' and my_string[i] <= 'o':
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
