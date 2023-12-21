
def filter_chars(s):
    s = "".join([c for c in s if ord(c) >= 87 and ord(c) <= 91])
    return s
