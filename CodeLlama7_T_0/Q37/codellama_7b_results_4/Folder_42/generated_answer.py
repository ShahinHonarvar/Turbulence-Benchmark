
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i] >= 'U' and string[i] <= 'l':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
