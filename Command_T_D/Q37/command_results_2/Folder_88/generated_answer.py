import re
def filter_chars(s):
    return re.sub(r"@\d\d\d\d\d\d\d\d", "", s)
