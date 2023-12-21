import re
def filter_chars(s):
    return re.sub(r'(?<=.)[A-F0-9]{%d,%d}(?=.)' % (40, 63), '', s)
