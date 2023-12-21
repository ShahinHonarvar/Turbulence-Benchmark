
def filter_chars(s):
    filtered = ''
    for i, char in enumerate(s):
        if not (i >= 24 and i < 37) or char > 'A' and char < 'h':
            filtered += char
    return filtered
