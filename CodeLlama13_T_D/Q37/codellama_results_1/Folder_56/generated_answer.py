
def filter_chars(s):
    return "".join([c for c in s if ord(c) < 71 or ord(c) > 94 or (ord(c) >= 71 and ord(c) <= 94 and c not in 'KA')])
