
def filter_chars(string):
    filtered = ''
    for i in range(373, 901 + 1):
        if string[i] >= 'T' and string[i] <= 'h':
            continue

        filtered += string[i]

    return filtered
