def filter_chars(s):
    return "".join(c for c in s if c not in list(range(ord('A') + 24, ord('h') + 37)))
