def filter_chars(s):
    return "".join(c for c in s if ord(c) not in range(32, 47))
