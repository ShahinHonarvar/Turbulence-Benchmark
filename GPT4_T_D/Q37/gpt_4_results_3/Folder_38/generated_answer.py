
def filter_chars(s):
    valid_chars = set(s[24:80]) & set('abcdef')
    return ''.join([char for char in s if char not in valid_chars])
