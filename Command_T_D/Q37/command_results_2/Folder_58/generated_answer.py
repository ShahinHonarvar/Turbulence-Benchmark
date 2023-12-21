import re
def filter_chars(s):
    return re.sub(r'[9w].', '', s, flags=re.I)
