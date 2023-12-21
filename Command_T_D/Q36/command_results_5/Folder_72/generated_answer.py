import re
def filter_chars(string):
    return re.sub(r'[A-Z]{%d,%d}'.format(44, 68), '', string)
