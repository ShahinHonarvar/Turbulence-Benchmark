import re
def filter_chars(s):
    return re.sub(r'(?i)([A-E]?)', r'\1', s, flags=re.I)
