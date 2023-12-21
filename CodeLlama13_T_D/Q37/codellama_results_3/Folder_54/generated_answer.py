
def filter_chars(s):
    return ''.join([c for c in s if 46 <= ord(c) <= 85 and '-' <= c <= 'X'])
