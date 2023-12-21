
def filter_chars(s):
    chars_to_remove = [char for char in s[52:76] if '5' < char < 'f']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
