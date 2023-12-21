
def filter_chars(s):
    return "".join([c for c in s if not (13 <= ord(c) <= 28 and 'c' <= c <= 'n')])
