
def filter_chars(my_string):
    filtered_string = ""
    for i in range(1, 8):
        if my_string[i] >= "L" and my_string[i] <= "a":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
