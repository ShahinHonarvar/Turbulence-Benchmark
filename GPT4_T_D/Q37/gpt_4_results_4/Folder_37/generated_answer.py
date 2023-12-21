
def filter_chars(s):
    to_remove = {char for char in s[17:64] if 'O' <= char <= '^'}
    return ''.join([char for char in s if char not in to_remove])
