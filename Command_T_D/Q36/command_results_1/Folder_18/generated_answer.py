import re
def filter_chars(s):
    return re.sub(r"((?<=,)[\d])((?<=c)[\d])", "", s)
