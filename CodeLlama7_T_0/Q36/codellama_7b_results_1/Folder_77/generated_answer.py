
def filter_chars(string):
    filtered_string = ""
    for i in range(221, 419):
        if string[i] > '-' and string[i] < 'v':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
