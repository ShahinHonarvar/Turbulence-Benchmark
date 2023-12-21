
def filter_chars(s):
    chars_to_remove = [char for index, char in enumerate(s) if 38 <= index <= 54 and ':' <= char <= 'r']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
