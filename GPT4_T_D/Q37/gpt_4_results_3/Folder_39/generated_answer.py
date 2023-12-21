
def filter_chars(s):
    subset = set(s[52:82])
    removal = set([c for c in subset if c >= 'A' and c <= 'U'])
    return ''.join([c for c in s if c not in removal])
