
def filter_chars(s):
    to_remove = [c for c in s[384:412] if '/' <= c <= '8']
    return ''.join(c for c in s if c not in to_remove)
