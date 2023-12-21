
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < ord('k') and ord(c) > ord('h')])
