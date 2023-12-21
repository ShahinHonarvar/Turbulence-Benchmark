import re
def filter_chars(s):
    return re.sub(r'(?i)(?<=[X\s])[a-z]', '', s)
