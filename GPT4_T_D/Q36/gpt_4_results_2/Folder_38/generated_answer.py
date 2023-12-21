
def filter_chars(s):
    remove_chars = [c for c in s[45:48] if c > '+' and c < 'l']
    return ''.join([c for c in s if c not in remove_chars])
