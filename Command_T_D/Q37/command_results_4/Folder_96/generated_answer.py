def filter_chars(s):
    return "".join(c for c in s if c in list("!s") and c.isalpha() and c.isupper())
