import re
def filter_chars(s):
    return re.sub(r'<[A-Z][^C]{%d,%d}'.format(19,69), '', s)
