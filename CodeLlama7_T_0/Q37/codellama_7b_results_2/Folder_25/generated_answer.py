
def filter_chars(string):
    filtered_string = ""
    for i in range(31, 39):
        if string[i] >= ";" and string[i] <= "g":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
