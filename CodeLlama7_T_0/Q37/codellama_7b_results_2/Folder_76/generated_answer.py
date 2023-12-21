
def filter_chars(string):
    filtered_string = ""
    for i in range(379, 899):
        if string[i] >= "M" and string[i] <= "v":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
