import re
def filter_chars(s):
    return re.sub(r'[D-H]', '', s)
