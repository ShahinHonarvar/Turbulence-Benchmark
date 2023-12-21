import re
def filter_chars(s):
    return re.sub(r'(?i)([A-Z]?)[A-Z]?(\d+)([A-Z]?)', r'\2', s)
