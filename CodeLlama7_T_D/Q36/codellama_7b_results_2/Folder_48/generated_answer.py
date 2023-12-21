
def filter_chars(my_string):
    filtered_string = ""
    for i in range(154, 222):
        if my_string[i] > "A" and my_string[i] < "f":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
