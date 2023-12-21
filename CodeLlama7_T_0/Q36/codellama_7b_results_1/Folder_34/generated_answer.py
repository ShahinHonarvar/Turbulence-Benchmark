
def filter_chars(string):
    filtered_string = ""
    for i in range(10, 79):
        if string[i] > "?" and string[i] < "m":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
