import re
def filter_chars(s):
    return re.sub(r'[A-Z]{%26,80}', '', s)
