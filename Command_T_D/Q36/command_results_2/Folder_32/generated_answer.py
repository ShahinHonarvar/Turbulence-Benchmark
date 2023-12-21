import re
def filter_chars(s):
    return re.sub(r'(?<=.)[A-Z]{%d,%d}{%d,%d}' % (40, 63, 7, 'H'), '', s)
