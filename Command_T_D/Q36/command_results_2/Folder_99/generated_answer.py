import re
def filter_chars(s):
    return re.sub(r'([\d|a|b|c|d])([\d|a|b|c|d])', r'\1', s)
