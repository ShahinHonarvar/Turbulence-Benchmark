
def filter_chars(s):
    remove_chars = [c for i, c in enumerate(s) if 26 <= i <= 64 and 'V' <= c <= 'o']
    return ''.join([c for c in s if c not in remove_chars])
