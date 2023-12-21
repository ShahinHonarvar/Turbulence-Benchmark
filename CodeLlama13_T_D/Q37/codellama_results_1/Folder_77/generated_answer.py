
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 384 or ord(c) > 411 or (ord(c) >= 47 and ord(c) <= 56)])
