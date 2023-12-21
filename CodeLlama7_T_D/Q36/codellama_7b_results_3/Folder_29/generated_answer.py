
def filter_chars(my_string):
    filtered_string = ""
    for i in range(46, 68):
        if my_string[i] > "H" and my_string[i] < "s":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
