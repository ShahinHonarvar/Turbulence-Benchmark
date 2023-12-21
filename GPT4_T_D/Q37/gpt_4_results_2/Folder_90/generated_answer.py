
def filter_chars(s):
    temp_chars = set([c for c in s[348:853] if 'J' <= c <= 'b'])
    return ''.join([c for c in s if c not in temp_chars])
