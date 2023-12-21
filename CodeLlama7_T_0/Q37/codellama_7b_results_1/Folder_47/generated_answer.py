
def filter_chars(string):
    filtered_string = ""
    for i in range(38, 54 + 1):
        if string[i] >= ':' and string[i] <= 'r':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
