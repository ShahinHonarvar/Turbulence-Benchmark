import re
def filter_chars(s):
    return re.sub(r'(?<=.)[A-J]{%d,%d}(?=.)' % (4, 8), '', s)
