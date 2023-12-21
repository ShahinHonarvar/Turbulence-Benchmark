import re
def filter_chars(s):
    return re.sub(r'(c[1-9]?)[a-z]{%13,28}(n[1-9]?)[a-z]{%13,28}' % (c, min(26, n - c), n), '', s)
