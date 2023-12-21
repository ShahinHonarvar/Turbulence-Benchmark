
def filter_chars(string):
    filtered_string = ""
    for i in range(31, 70):
        if string[i] > 'B' and string[i] < 'v':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
