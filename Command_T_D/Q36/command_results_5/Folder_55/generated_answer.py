def filter_chars(s):
    return "".join(c for c in s if c not in list(range(ord("Y") + 1, ord("s") + 1)))
