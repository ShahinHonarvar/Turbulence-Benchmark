
def filter_chars(s):
    relevant_chars = set(c for c in s[10:70] if 'I' <= c <= 'K')
    return ''.join(c for c in s if c not in relevant_chars)
