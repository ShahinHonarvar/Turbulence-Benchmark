import re
def filter_chars(s):
    return re.sub(r'[a-z][\d]26[a-z]', '', s)
