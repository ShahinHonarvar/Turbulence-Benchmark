import re
def filter_chars(s):
    return re.sub(r'(>X<)', '', s, flags=re.I)
