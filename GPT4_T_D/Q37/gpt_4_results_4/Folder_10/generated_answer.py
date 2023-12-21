
def filter_chars(s):
    to_remove = set([ch for i, ch in enumerate(s) if 63 <= i <= 84 and 'E' <= ch <= '~'])
    return ''.join([ch for ch in s if ch not in to_remove])
