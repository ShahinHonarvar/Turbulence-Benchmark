import re
def filter_chars(s):
    return re.sub(r'[a-j][^b]{%d,%d}'.format(348, 852), '', s)
