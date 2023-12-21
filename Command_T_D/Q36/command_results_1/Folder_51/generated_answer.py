import re
def filter_chars(s):
    return re.sub(r'([58-81])\b', r'\1', s)
