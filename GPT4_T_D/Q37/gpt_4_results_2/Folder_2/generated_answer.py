
def filter_chars(s):
    chars_to_remove = set(filter(lambda x: ',' <= x <= 'V', s[477:985]))
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s
