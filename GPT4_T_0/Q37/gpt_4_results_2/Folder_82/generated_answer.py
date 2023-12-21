
def filter_chars(s):
    chars_to_remove = [char for char in s[12:26] if 'P' <= char <= 'x']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
