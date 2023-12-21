import re
def filter_chars(s):
    return re.sub(r"([A-z])", r" ", s, flags=re.I)
