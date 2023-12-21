
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if (502 < i < 946) and (char > 'W' and char < 'y'):
            continue

        else:

            filtered_string += char

    return filtered_string
