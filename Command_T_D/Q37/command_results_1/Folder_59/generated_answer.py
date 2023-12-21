import re
def filter_chars(s):
    return re.sub(r'([\d_]+)(_+)', r'\1', s)
