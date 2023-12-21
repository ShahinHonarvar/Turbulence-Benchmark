import re
def filter_chars(s):
    return re.sub(r'(?<=.)[A-Z][a-z]{%d,%d}'.format(41, 86), '', s)
