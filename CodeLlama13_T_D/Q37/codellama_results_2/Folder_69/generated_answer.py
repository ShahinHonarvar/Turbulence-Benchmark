
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 114 or ord(c) > 639 or not (ord('!') <= ord(c) <= ord('x'))])
