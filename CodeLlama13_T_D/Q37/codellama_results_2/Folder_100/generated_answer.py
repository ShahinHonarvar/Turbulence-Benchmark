
def filter_chars(s):
    return ''.join([c for c in s if not (ord('J') <= ord(c) <= ord('Q'))])
