
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if (i >= 2 and i <= 6) and (string[i] >= '?' and string[i] <= 'f'):
            continue

        filtered_string += string[i]

    return filtered_string
