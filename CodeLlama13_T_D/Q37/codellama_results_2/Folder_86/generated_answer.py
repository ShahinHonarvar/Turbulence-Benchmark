
def filter_chars(s):
    return ''.join([c for c in s if (ord(c) >= ord('O') and ord(c) <= ord('}'))])
