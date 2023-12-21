import re
def filter_chars(s):
    return re.sub(r'([7-e])([22-85])', r'\1\2', s)
