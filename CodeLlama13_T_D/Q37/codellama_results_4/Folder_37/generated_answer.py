
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 17 or ord(c) > 63 or (ord('O') <= ord(c) <= ord('^'))])
