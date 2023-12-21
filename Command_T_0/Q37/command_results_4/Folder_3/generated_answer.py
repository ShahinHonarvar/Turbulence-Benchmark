import re
def filter_chars(s):
    return re.sub(r'[A-Z][37-56]_[A-Z]', '', s)
