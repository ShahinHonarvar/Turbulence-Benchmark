
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 98 or ord(c) > 35])
