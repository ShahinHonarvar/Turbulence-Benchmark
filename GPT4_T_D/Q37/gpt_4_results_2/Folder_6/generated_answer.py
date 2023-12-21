
def filter_chars(s):
    to_remove = set()
    for i in range(13, min(29, len(s))):
        if 'c' <= s[i] <= 'n':
            to_remove.add(s[i])
    return ''.join(c for c in s if c not in to_remove)
