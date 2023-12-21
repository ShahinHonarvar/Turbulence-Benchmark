import re
def filter_chars(s):
    return re.sub(r'[c-i]', '', s)
