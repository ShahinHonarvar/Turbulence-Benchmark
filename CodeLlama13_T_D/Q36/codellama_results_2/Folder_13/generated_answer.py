
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 526 or ord(c) > 323])
