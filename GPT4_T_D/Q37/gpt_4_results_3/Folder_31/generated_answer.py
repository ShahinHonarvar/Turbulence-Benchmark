
def filter_chars(s):
    target_chars = {char for i, char in enumerate(s) if 57 <= i <= 96 and '<' <= char <= 'w'}
    return ''.join([char for char in s if char not in target_chars])
