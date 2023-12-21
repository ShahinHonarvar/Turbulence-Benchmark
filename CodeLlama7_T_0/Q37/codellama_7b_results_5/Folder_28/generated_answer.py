
def filter_chars(string):
    filtered_string = ""
    for i in range(20, 80):
        if string[i] >= "!" and string[i] <= "T":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
