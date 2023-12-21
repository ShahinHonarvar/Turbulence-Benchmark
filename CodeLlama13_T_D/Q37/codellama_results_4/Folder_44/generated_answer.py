
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 56 and ord(c) > 42])
