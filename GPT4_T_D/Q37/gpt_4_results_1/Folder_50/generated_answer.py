
def filter_chars(s):
    target_chars = set([char for i, char in enumerate(s) if 71 <= i <= 96 and '_' <= char <= 'o'])
    return ''.join([char for char in s if char not in target_chars])
