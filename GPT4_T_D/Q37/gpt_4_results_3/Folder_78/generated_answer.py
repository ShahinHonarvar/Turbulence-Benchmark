
def filter_chars(s):
    set_chars = set([i for i in s[75:100] if '8' <= i <= 'e'])
    return ''.join([char for char in s if char not in set_chars])
