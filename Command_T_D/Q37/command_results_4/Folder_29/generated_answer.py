import re
def filter_chars(s):
    return re.sub(r'&[1-9][0-9]v', '', s)
