import re
def filter_chars(s):
    return re.sub(r'(?i)(?<=[a-z])[A-Z][^A-Z\s)]', r'\1', s)
