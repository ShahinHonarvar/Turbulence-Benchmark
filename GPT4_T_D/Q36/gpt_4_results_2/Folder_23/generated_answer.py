
def filter_chars(s):
    chars_to_remove = [char for char in s[22:25] if '5' < char < '}']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
