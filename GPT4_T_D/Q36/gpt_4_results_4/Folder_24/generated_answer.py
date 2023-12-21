
def filter_chars(s):
    chars_to_remove = [char for char in s[11:15] if 't' < char < 'v']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
