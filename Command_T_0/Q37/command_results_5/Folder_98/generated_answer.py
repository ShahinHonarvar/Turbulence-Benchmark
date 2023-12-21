import re
def filter_chars(s):
    return re.sub(r'[Rr]e[a-t]', '', s)
