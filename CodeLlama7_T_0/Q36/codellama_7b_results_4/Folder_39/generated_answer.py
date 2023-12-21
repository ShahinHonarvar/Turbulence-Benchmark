
def filter_chars(string):
    filtered_string = ""
    for i in range(43, 59):
        if string[i] > '5' and string[i] < 'C':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
