import re
def filter_chars(s):
    return re.sub(r'([A-Z])', r'3', s, flags=re.I)
