
def filter_chars(s):
    return ''.join([c for c in s if (ord(c) < ord('G')) or (ord(c) > ord('p'))])
