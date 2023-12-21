import re
def filter_chars(s):
    return re.sub(r'[&v]', '', s, flags=re.I)
