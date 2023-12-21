
def filter_chars(string):
    filtered_string = ""
    for i in range(42, 68):
        if string[i] > 't' and string[i] < 'x':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
