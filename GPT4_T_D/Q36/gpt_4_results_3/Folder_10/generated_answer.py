
def filter_chars(s):
    chars_to_remove = [char for char in s[36:60] if '!' < char < 'B']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
