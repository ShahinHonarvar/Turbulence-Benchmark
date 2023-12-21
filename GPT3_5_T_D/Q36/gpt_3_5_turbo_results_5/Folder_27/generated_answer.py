
def filter_chars(string):
    return ''.join([c for c in string if not (ord('6') < ord(c) < ord('_'))])
