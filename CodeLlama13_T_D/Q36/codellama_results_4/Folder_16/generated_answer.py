
def filter_chars(s):
    chars = []
    for i in range(331, 713):
        if s[i].isupper() and s[i] != '_':
            chars.append(s[i])
    return ''.join([c for c in s if c not in chars])
