import re
def filter_chars(s):
    return re.sub(r'[A-z]{%d,%d}'.format(318, 337), '', s)
