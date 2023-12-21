
def filter_chars(string):
    filtered = ''
    for i, char in enumerate(string):
        if i >= 27 and i <= 85 and 'c' <= char <= 'i':
            continue
        else:
            filtered += char
    return filtered
