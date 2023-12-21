import re
def filter_chars(s):
    return re.sub(r'[^?f].{2,5}[^?f]', '', s)
