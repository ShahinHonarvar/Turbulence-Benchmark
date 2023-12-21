def filter_chars(s):
    return "".join(c for i, c in enumerate(s) if (i > 75 and i < 99) and (c >= '8' and c <= 'e'))
