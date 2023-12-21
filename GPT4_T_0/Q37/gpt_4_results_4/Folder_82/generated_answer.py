
def filter_chars(s):
    chars_to_remove = [char for char in s[12:26] if 'P' <= char <= 'x']
    return ''.join([char for char in s if char not in chars_to_remove])
