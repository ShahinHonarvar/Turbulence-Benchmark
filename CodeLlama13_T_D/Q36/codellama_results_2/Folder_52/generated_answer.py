
def filter_chars(s):
    return ''.join([c for c in s if not (ord('I') < ord(c) < ord('a'))])
