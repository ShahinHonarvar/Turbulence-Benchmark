
def filter_chars(s):
    chars_to_remove = set([ch for ch in s[12:89] if '&' <= ch <= 'v'])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
