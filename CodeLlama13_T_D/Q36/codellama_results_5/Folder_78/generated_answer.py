
def filter_chars(s):
    filtered = ''
    for i, c in enumerate(s):
        if 29 <= i < 33 and ord('%') < ord(c) < ord('a'):
            continue
        filtered += c
    return filtered
