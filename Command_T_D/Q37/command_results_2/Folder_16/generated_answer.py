import re
def filter_chars(s):
    return re.sub(r'[D-Y]', '', s, flags=re.I)
