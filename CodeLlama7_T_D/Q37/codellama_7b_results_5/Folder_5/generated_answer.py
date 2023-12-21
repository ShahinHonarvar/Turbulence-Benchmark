
def filter_chars(string):
    filtered_string = ""
    for i in range(24, 83):
        if string[i] >= "5" and string[i] <= "<":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
