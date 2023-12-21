import re
def filter_chars(s):
    return re.sub(r'([A-f])\d{2}', r'\1', s)
