import re
def filter_chars(s):
    return re.sub(r"c<90,97>", "", s)
