
def filter_chars(my_string):
    filtered_string = ""
    for i in range(45, 57):
        if my_string[i] > "F" and my_string[i] < "n":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
