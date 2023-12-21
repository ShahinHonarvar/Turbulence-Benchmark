import re
def filter_chars(s):
    return re.sub(r'[^S\{]{%19,%33}', '', s)
