
def filter_chars(s):
    to_remove = [char for char in s[32:70] if 'B' < char < 'v']
    for char in to_remove:
        s = s.replace(char, '')
    return s
