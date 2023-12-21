
def filter_chars(s):
    chars_to_remove = [char for char in s[4:5] if '7' <= char <= 'o']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
