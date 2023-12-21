
def filter_chars(s):
    to_remove = set([c for c in s[503:754] if '9' <= c <= 'w'])
    return ''.join([c for c in s if c not in to_remove])
