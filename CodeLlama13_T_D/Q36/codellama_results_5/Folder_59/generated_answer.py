
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 107 and ord(c) > 63])
