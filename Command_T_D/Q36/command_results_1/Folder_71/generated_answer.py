import re
def filter_chars(s):
    return re.sub(r'(?i)(\d[A-Z])', '', s)
