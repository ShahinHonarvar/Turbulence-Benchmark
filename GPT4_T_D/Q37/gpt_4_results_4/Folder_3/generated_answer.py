
def filter_chars(s):
    substring_to_check = s[37:57]
    chars_to_remove = [char for char in substring_to_check if '6' <= char <= '_']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
