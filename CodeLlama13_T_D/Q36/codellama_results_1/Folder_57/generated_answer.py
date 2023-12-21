
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 75 and ord(c) > 64])
