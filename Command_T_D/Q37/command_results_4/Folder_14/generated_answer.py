import re
def filter_chars(s):
    return re.sub(r'(?<=\d)[a-b]{%d,%d}'.format(35, 98), '', s)
