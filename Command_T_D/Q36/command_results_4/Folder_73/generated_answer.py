import re
def filter_chars(s):
    return re.sub(r'(?!#)[\dT]6789', '', s)
