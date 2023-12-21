import re
def filter_chars(s):
    return re.sub(r'[fho]23456789', '', s)
