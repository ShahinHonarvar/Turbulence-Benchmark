
def filter_chars(s):
    chars_to_remove = [char for char in s[56:80] if 'S' < char < 's']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
