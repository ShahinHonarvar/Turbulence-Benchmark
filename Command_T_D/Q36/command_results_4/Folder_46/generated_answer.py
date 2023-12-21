def filter_chars(s):
    s = s[:19] + s[69:]
    return "<".join(s) + ">"
