
def filter_chars(s):
    chars_to_remove = [ch for ch in s[46:86] if '-' <= ch <= 'X']

    for ch in chars_to_remove:
        s = s.replace(ch, '')

    return s
