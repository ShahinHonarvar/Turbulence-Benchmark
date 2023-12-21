
def filter_chars(s):
    chars_to_remove = [char for char in s[2:4] if '5' <= char <= '_']
    return ''.join(char for char in s if char not in chars_to_remove)
