
def filter_chars(string):
    filtered_string = ""
    for i in range(51, 76):
        if string[i] > '5' and string[i] < 'f':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
