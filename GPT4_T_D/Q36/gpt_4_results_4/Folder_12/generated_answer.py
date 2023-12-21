
def filter_chars(s):
    chars_to_remove = [char for char in s[33:84] if 'm' < char < 'w']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
