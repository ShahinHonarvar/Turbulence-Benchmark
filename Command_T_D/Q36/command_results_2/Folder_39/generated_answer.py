import re
def filter_chars(string):
    return re.sub(r'[A-E]{%d,%d}'.format(43, 59), '', string)
