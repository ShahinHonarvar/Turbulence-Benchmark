
def filter_chars(s):
    return ''.join([c for c in s if not (ord('F') < ord(c) < ord('O'))])
