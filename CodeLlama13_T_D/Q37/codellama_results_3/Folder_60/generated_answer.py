
def filter_chars(s):
    return ''.join([c for c in s if not (12 <= ord(c) <= 77 and ':' <= c <= 'L')])
