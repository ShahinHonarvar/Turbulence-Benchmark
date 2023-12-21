import re
def filter_chars(s):
    return re.sub(r'([A-E])\d{3}', r'\1', s)
