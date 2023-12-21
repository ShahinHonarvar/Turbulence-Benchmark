
def filter_chars(s):
    filtered = ''
    for i, c in enumerate(s):
        if 3 <= i < 5 and ord('Y') < ord(c) < ord('s'):
            filtered += c
        else:
            filtered += c
    return filtered
