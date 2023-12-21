def filter_chars(s):
    return "".join(c for c in s if c in range(ord('a')+1, ord('A')+1, 1))
