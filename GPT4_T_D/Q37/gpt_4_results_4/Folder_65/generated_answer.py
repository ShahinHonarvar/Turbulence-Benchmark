
def filter_chars(s):
    to_remove = [c for c in s[61:71] if '0' <= c <= '@']
    return ''.join(c for c in s if c not in to_remove)
