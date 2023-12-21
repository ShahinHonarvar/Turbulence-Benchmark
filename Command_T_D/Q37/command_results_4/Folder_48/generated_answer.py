def filter_chars(s):
    return "".join(c for c in s if c.isalpha() and ord(c) >= ord("q") and ord(c) <= ord("z"))
