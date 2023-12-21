
def filter_chars(s):
    return ''.join([c for c in s if (ord(c) > ord('f') and ord(c) < ord('{'))])
