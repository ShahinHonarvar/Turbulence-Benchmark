def filter_chars(s):
    return ''.join(x for x in s if not (x in s) and x not in list(range(15, 85)))
