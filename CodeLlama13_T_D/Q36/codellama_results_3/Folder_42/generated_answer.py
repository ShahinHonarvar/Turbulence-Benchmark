
def filter_chars(s):
    return ''.join([c for c in s if not (42 < ord(c) < 68 and c > 't' and c < 'x')])
