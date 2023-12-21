
def filter_chars(my_string):
    filtered_string = ""
    for i in range(55, 66):
        if my_string[i] > "f" and my_string[i] < "|":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
