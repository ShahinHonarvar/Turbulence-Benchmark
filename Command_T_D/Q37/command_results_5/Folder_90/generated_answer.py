import re
def filter_chars(s):
    return re.sub(r'[a-j][b-z]', '', s)
