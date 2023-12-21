
def filter_chars(s):
    return "".join([c for c in s if (ord(c) < 52 or ord(c) > 81) and (ord(c) < ord('A') or ord(c) > ord('U'))])
