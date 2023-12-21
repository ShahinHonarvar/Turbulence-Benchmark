
def filter_chars(string):
    filtered_string = ""
    for i in range(29, 97 + 1):
        if string[i] >= '-' and string[i] <= 'n':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
