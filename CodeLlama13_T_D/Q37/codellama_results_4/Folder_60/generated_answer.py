
def filter_chars(string):
    return "".join([c for c in string if 12 <= ord(c) <= 77 and ':' <= c <= 'L'])
