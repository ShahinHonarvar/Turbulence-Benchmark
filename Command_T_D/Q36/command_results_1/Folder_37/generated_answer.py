import re
def filter_chars(s):
    return re.sub(r'[4567]','',s)
