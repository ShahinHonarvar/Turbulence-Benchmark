def filter_chars(s):
    return "".join(x for x in s if x not in list(range(3,65)))
