
def filter_chars(s):
    unique_chars = set(s[319:337])
    valid_chars = [char for char in unique_chars if 'B' < char <'z']
    for char in valid_chars:
        s = s.replace(char, '')
    return s
