
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 52 and ord(c) > 10])
