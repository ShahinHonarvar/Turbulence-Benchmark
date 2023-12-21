
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if string[i] >= '6' and string[i] <= 'w':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
