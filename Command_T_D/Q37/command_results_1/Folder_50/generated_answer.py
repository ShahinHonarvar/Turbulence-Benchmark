def filter_chars(s):
    return "".join(c for c in s if c.isalpha() and c.lower() in range(71, 96, 1))
