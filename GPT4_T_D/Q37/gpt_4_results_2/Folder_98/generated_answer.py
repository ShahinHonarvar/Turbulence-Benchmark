
def filter_chars(s):
    chars_to_remove = [char for char in s[8:10] if 'R' <= char <= 't']
    return ''.join(char for char in s if char not in chars_to_remove)
