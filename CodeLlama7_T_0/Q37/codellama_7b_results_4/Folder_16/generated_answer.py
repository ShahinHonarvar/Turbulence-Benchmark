
def filter_chars(string):
    filtered_string = ""
    for i in range(225, 381 + 1):
        if string[i] >= 'D' and string[i] <= 'Y':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
