import re
def filter_chars(s):
    return re.sub(r'([Ww] | [Z z])', '', s, flags=re.I)
