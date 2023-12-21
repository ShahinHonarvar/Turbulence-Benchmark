import re
def filter_chars(str):
    return re.sub(r'[A-Z][a-z]{%d,%d}'.format(23, 89), '', str)
