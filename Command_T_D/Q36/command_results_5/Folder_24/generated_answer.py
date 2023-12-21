import re
def filter_chars(s):
    return re.sub(r'[a-d]11', r'g', s)
