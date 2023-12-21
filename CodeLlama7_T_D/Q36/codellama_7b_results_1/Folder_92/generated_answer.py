
def filter_chars(string):
    filtered = ""
    for i in range(1, len(string)):
        if string[i] > ',' and string[i] < 'f':
            continue

        else:

            filtered += string[i]

    return filtered
