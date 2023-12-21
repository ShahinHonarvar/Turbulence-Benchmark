
def filter_chars(s):
    chars_to_remove = [char for char in s[39:80] if '.' < char < '^']
    for char in set(chars_to_remove):
        s = s.replace(char, '')
    return s
