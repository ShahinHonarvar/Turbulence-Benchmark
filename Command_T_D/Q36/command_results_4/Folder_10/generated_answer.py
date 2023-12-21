def filter_chars(str):
    return "".join(c for c in str if 35 <= ord(c) <= 60)
