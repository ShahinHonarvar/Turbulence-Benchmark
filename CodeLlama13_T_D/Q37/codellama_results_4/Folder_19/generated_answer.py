
def filter_chars(s):
    return ''.join([c for c in s if 35 <= ord(c) <= 89 and 'E' <= c <= 't'])
