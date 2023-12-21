import re
def filter_chars(s):
    return re.sub(r'([^Fh])+', '', s, flags=re.I)
