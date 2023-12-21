import re
def filter_chars(s):
    return re.sub(r'(?!\d)7[a-d]e', '', s)
