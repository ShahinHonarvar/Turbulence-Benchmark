
def filter_chars(s):
    subset = set([char for idx, char in enumerate(s) if 19 <= idx <= 32 and 'f' <= char <= 'o'])
    return ''.join([char for char in s if char not in subset])
