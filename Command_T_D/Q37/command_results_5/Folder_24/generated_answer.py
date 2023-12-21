import re
def filter_chars(s):
    return re.sub(r'[2-s]{%36,79}', '', s)
