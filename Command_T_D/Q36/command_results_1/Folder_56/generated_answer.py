import re
def filter_chars(s):
    return re.sub(r'(?<=.)[A-Z]{%d}'.format(31,50), '', s)
