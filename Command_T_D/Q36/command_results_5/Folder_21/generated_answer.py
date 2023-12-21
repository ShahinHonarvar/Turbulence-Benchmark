import re
def filter_chars(s):
    return re.sub(r'(?i)([2-6])', r'\1', s)
