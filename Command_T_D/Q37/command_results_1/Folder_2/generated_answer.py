import re
def filter_chars(s):
    return re.sub(r"[\d,A-Z][\d,A-Z]", "", s)
