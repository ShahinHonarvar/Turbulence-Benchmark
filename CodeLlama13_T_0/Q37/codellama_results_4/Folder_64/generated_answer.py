
def filter_chars(s):
    return ''.join([c for c in s if not (ord('L') <= ord(c) <= ord('a'))])
