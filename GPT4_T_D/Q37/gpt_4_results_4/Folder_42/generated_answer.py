
def filter_chars(s):
    chars_to_remove = [char for char in s[73:75] if 'U' <= char <= 'l']
    return ''.join(char for char in s if char not in chars_to_remove)
