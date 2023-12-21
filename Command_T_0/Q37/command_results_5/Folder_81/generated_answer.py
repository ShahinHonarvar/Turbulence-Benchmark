import re
def filter_chars(s):
    return re.sub(r'[8-m]', '', s)
