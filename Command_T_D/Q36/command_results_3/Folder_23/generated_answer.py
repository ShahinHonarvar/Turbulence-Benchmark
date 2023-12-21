import re
def filter_chars(s):
    return re.sub(r'([A-Z])\d{3}([A-Z])', r'\1\4', s)
