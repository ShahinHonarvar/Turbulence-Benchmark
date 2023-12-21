
def filter_chars(string):
    filtered = ""
    for i in range(77, 87):
        if string[i] > ';' and string[i] < 'r':
            continue

        else:

            filtered += string[i]

    return filtered
