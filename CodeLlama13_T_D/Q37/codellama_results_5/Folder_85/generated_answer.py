
def filter_chars(s):
    return "".join([c for c in s if not (28 <= ord(c) <= 65 and 'O' <= c <= 'd')])
