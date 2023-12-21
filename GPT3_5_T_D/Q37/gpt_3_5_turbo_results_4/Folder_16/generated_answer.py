
def filter_chars(string):
    filtered = ''
    for i, char in enumerate(string):
        if 225 <= i <= 381 and 'D' <= char <= 'Y':
            continue
        filtered += char
    return filtered
