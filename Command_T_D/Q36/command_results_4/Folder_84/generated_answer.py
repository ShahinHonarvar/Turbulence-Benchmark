import re
def filter_chars(s):
    return re.sub(r"<c-s>(?<=171,636)", "", s)
