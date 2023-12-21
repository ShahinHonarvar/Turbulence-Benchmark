
def filter_chars(string):
    filtered = ''
    for i in range(len(string)):
        if string[i] >= 'A' and string[i] <= 'U':
            continue

        filtered += string[i]

    return filtered
