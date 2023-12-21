
def filter_chars(s):
    chars = set(s[i] for i in range(31, min(39, len(s))) if ';' <= s[i] <= 'g')
    return ''.join(c for c in s if c not in chars)
