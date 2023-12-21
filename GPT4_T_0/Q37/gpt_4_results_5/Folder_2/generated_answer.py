
def filter_chars(s):
    chars_to_remove = set([c for c in s[477:985] if ',' <= c <= 'V'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
