
def filter_chars(string):
    filtered_string = ""
    for i in range(24, 37):
        if string[i] > 'A' and string[i] < 'h':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
