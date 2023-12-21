
def filter_chars(string):
    filtered_string = ""
    for i in range(669, 888):
        if string[i] > 'B' and string[i] < 'Y':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
