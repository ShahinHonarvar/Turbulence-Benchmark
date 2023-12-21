import re
def filter_chars(s):
    return re.sub(r'[A-D]44-68', '', s)
