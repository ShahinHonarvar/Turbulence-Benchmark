
def filter_chars(s):
    chars = set()
    for i in range(73, 75):
        if s[i] >= 'U' and s[i] <= 'l':
            chars.add(s[i])
    return ''.join([c for c in s if c not in chars])
