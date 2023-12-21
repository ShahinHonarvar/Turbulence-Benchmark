
def filter_chars(s):
    remove_chars = set(s[i] for i in range(28, min(66, len(s))) if 'O' <= s[i] <= 'd')
    return ''.join([c for c in s if c not in remove_chars])
