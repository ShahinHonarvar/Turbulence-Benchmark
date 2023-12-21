import re
def filter_chars(s):
    return re.sub(r"([P-x]){12,25}", "", s)
