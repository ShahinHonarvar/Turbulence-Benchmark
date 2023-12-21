def filter_chars(s):
    return "".join(c for c in s if not (c >= '.' and c <= 'b' and c in range(72, 94)))
