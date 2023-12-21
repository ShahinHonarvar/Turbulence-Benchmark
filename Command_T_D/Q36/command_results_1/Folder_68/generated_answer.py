import re
def filter_chars(s):
    return re.sub(r'([1-9])([a-z])', r'\1', s)
