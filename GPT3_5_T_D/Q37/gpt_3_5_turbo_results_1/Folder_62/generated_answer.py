
def filter_chars(s):
    new_str = ''
    for i, char in enumerate(s):
        if 10 <= i <= 69 and 'I' <= char <= 'K':
            continue
        new_str += char
    return new_str
