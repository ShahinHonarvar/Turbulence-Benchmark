import re
def filter_chars(s):
    return re.sub(r"[\u0032-\u0084].[a-w]", "", s)
