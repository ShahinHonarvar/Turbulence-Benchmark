
def filter_chars(string):
    filtered_string = ""
    for i in range(603, 759 + 1):
        if string[i] >= 'Q' and string[i] <= 'h':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
