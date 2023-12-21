
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i] >= '@' and string[i] <= 'p':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
