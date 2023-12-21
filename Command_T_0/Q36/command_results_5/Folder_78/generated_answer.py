import re
def filter_chars(s):
    return re.sub(r'[A-Z]{%29,%33}', '', s)
