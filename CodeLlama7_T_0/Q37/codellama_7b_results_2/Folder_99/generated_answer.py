
def filter_chars(string):
    filtered_string = ""
    for i in range(373, 901 + 1):
        if string[i] >= 'T' and string[i] <= 'h':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
