
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 72 or ord(c) > 94])
