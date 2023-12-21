
def filter_chars(string):
    filtered = ''
    for i, char in enumerate(string):
        if 18 <= i < 95 and 'K' < char < 'a':
            continue
        filtered += char
    return filtered
