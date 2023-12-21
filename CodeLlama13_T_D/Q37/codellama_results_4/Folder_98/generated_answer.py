
def filter_chars(s):
    return ''.join([c for c in s if (8 <= ord(c) <= 9 and c >= 'R' and c <= 't')])
