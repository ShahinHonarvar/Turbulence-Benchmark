
def filter_chars(s):
    return s[:12] + s[12:89].replace('&', '').replace("'", '') + s[89:]
