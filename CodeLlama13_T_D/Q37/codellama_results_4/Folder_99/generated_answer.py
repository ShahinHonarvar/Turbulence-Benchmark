
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 902 and ord(c) > 372])
