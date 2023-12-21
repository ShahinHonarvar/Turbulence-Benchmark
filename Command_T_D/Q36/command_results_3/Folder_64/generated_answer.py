import re
def filter_chars(s):
    return re.sub(r'([\d]+)3([\d]+)[^7]', r'\1', s)
