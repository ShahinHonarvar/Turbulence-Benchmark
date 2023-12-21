
def filter_chars(string):
    filtered = ''
    for i, char in enumerate(string):
        if 502 <= i < 946 and 'W' < char < 'y':
            continue
        filtered += char
    return filtered
