import re
def filter_chars(str):
    return re.sub(r'[A-Z]{%d,%d}'.format(1,7), '', str)
