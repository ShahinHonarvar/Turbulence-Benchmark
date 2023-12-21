
def filter_chars(my_string):
    filtered_string = ""
    for i in range(41, 56):
        if my_string[i].isalpha() and my_string[i].lower() > "z" and my_string[i].lower() < "c":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
