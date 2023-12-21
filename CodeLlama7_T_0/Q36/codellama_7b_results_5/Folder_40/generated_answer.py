
def filter_chars(string):
    filtered_string = ""
    for i in range(1, len(string)):
        if string[i] > '-' and string[i] < 'L':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
