import re
def filter_chars(s):
    return re.sub(r'([1-7])', r'\1', s)
