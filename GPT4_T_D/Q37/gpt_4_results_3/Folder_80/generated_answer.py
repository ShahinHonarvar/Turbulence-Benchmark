
def filter_chars(s):
    filter_chars = {char for char in s[36:80] if 'a' <= char <= 'i'}
    return ''.join(char for char in s if char not in filter_chars)
