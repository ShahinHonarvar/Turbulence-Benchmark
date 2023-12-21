import re
def filter_chars(s):
    return re.sub(r'[Gq]', '', s, flags=re.I)
