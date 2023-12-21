import re
def filter_chars(s):
    return re.sub(r"([A-Q]{38,99})", "", s)
