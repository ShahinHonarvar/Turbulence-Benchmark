import re
def filter_chars(s):
    return re.sub(r'(?i)([A-Z])([81-86])([A-Z])', r'\1!', s)
