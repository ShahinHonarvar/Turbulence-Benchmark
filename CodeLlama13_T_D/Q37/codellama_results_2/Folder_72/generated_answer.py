
def filter_chars(s):
    return ''.join([c for c in s if not (35 <= ord(c) <= 51 and 'H' <= c <= 's')])
