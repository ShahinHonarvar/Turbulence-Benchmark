
def filter_chars(s):
    chars_to_remove = [char for char in s[17:64] if 'O' <= char <= '^']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
