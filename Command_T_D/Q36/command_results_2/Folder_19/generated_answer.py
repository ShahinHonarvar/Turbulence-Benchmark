import re
def filter_chars(s):
    return re.sub(r'[^\s];[a-z]{%d}[^a-z]{%d}'.format(77, 87), '', s)
