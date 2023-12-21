def filter_chars(s):
    return "".join(c for c in s if c not in list(range(86, 93)))
