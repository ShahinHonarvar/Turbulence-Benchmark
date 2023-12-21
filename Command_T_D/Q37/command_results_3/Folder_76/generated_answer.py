def filter_chars(s):
    return "".join(c for c in s if ord(c) in range(379, 898, 1) and c in range('M', 'v'))
