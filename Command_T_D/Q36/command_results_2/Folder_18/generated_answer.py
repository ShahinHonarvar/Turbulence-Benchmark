import re
def filter_chars(s):
    return re.sub(r'[a-zA-Z]([5-8][0-9])([a-zA-Z]?)[0-9]5', r'\1\3', s)
