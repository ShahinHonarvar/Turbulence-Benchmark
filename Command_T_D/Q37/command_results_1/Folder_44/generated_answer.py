import re
def filter_chars(s):
    return re.sub(r'(([+\d])\d{3})', r'\1', s)
