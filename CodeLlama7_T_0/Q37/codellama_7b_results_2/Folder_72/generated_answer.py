
def filter_chars(string):
    filtered_string = ""
    for i in range(35, 52):
        if string[i] >= "H" and string[i] <= "s":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
