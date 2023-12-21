import re
def filter_chars(s):
    return re.sub(r'[A-Z][a-c]', '', s)
