
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 23 or ord(c) > 89 or ord(c) <= 122])
