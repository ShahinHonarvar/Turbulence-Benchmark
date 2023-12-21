
def filter_chars(s):
    affected_chars = set([char for i, char in enumerate(s) if 42 <= i <= 92 and '/' <= char <= 'a'])
    return ''.join([char for char in s if char not in affected_chars])
