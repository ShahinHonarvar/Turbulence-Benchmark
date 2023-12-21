def filter_chars(s):
    return "".join(x for x in s if x in range(ord('W'), ord('{') + 1))
