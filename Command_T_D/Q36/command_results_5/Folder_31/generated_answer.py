import re
def filter_chars(s):
    return re.sub(r'[A-K]{%14,%75}', '', s)
