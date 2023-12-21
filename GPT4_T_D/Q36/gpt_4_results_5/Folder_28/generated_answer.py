
def filter_chars(s):
    chars_to_remove = {char for char in s[32:73] if 'M' < char < 'j'}
    return ''.join(c for c in s if c not in chars_to_remove)
