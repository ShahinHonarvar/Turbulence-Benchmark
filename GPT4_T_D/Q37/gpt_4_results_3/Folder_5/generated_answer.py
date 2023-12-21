
def filter_chars(s):
    chars_to_remove = [x for x in s[24:83] if '5' <= x <= '<']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
