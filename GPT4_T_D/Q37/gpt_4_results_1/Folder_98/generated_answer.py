
def filter_chars(s):
    to_remove = set([char for char in s[8:10] if 'R' <= char <= 't'])
    return ''.join([char for char in s if char not in to_remove])
