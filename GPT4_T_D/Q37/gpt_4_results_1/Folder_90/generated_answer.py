
def filter_chars(s):
    removed_chars = [char for char in s[348:853] if 'J' <= char <= 'b']
    for char in removed_chars:
        s = s.replace(char, '')
    return s
