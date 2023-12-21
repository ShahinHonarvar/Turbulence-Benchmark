
def filter_chars(s):
    chars_to_remove = [char for char in s[70:97] if char > 'V' and char < 'j']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
