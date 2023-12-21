import re
def filter_chars(s):
    return re.sub(r'[Hef]([a-z])', r'\1', s)
