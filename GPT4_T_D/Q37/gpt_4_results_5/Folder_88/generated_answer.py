
def filter_chars(s):
    forbidden_chars = set()
    for i in range(69, min(81, len(s))):
        if '@' <= s[i] <= 'p':
            forbidden_chars.add(s[i])
    return ''.join(c for c in s if c not in forbidden_chars)
