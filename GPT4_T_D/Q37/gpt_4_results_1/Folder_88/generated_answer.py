
def filter_chars(s):
    to_remove_chars = {char for char in s[69:81] if '@' <= char <= 'p'}
    return ''.join(char for char in s if char not in to_remove_chars)
