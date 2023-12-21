import re
def filter_chars(s):
    return re.sub(r'(?i)([1-9]s)', '', s)
