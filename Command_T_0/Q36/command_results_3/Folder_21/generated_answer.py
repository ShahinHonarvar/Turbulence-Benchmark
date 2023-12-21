import re
def filter_chars(s):
    return re.sub(r'[2-7]', '', s)
