import re
def filter_chars(s):
    return re.sub(r"<[A-s]>[35:51]", "", s)
