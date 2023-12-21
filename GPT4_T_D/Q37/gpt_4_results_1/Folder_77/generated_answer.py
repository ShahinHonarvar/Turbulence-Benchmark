
def filter_chars(s):
    remove_chars = [c for c in s[384:412] if '/' <= c <= '8']
    return ''.join([c for c in s if c not in remove_chars])
