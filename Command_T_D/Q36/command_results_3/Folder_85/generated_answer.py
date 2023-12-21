def filter_chars(s):
    return "".join(c for c in s if c < "S" or c > "s")
