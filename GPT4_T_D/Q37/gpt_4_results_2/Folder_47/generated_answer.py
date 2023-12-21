
def filter_chars(s):
    to_remove = [c for c in s[38:55] if ':' <= c <= 'r']
    return ''.join(c for c in s if c not in to_remove)
