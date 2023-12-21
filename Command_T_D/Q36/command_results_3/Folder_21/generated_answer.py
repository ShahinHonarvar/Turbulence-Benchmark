import re
def filter_chars(s):
    return re.sub(r'(?i)([A-Z])([2-9])', r'\1', s)
