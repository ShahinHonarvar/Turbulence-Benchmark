
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 521 or ord(c) > 722 or not (ord(c) >= 62 and ord(c) <= 95)])
