import re
def filter_chars(s):
    return re.sub(r'[K-m]', '', s, flags=re.I)
