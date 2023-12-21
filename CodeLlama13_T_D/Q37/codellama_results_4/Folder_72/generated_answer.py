
def filter_chars(string):
    return "".join([c for c in string if not (ord('H') <= ord(c) <= ord('s'))])
