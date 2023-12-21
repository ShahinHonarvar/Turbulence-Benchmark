
def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 57 <= i <= 96 and '<' <= char <= 'w']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
