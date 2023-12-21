import re
def filter_chars(s):
    return re.sub(r'[A-U][\d]{1,2}', '', s)
