
def filter_chars(string):
    filtered = ''
    for i, char in enumerate(string):
        if 373 <= i <= 901 and 'T' <= char <= 'h':
            continue

        filtered += char

    return filtered
