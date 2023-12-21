import re
def filter_chars(s):
    return re.sub(r'[jve]{%d,%d}'.format(54, 83), '', s)
