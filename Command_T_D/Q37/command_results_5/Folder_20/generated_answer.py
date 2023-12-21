import re
def filter_chars(s):
    return re.sub(r'[a-z][\d]25[a-z][\d]97[a-z][\d]', '', s)
