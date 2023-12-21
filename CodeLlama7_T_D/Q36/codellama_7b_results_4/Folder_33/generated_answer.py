
def filter_chars(my_string):
    filtered_string = ""
    for i in range(299, 418):
        if my_string[i] > "9" and my_string[i] < "P":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
