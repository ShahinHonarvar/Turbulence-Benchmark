
def filter_chars(s):
    chars_to_remove = [char for char in s[7:9] if 'B' <= char <= 'H']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
