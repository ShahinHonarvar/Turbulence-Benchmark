
def filter_chars(s):
    return ''.join([c for c in s if not (ord(c) >= 75 and ord(c) <= 99 and ord(c) >= 8 and ord(c) <= 14)]).
