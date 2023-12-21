import re
def filter_chars(s):
    return re.sub(r'[^W\d].|\d[^y]+', '', s)
