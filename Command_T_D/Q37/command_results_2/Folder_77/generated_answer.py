def filter_chars(s):
    return s[:384] + s[385:-11] + s[-11:]
