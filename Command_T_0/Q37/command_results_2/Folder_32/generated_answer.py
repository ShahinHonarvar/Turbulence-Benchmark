import re
def filter_chars(s):
    return re.sub(r'[A-Z][a-z]{23,89}', '', s)
