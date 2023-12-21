
def filter_chars(my_string):
    filtered_string = ""
    for i in range(4, 8):
        if my_string[i] > "1" and my_string[i] < "J":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
