
def filter_chars(s):
    char_to_remove = [c for c in s[4:5] if '7' <= c <= 'o']
    return ''.join([c for c in s if c not in char_to_remove])
