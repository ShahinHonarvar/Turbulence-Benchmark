def filter_chars(s):
    return "".join(c for c in s if c in range(ord('A') + 26, ord('z') + 1))
