
def filter_chars(s):
    chars_to_remove = set([char for char in s[21:44] if '+' <= char <= '8'])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
