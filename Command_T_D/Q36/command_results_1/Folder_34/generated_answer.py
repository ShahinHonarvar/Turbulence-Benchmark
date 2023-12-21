import re
def filter_chars(s):
    return re.sub(r'[^?m]{%10,79}', '', s)
