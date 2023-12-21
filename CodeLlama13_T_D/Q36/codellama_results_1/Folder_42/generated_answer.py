
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 120 and ord(c) > 84])
