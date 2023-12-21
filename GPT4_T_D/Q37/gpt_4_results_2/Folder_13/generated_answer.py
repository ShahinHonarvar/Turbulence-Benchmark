
def filter_chars(s):
    to_remove = set([char for i, char in enumerate(s) if 124 <= i <= 854 and '9' <= char <= 's'])
    return ''.join([char for char in s if char not in to_remove])
