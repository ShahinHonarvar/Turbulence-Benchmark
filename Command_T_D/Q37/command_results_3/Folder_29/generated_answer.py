import re
def filter_chars(s):
    return re.sub(r'[&\d]:[&v]{%d,%d}'.format(12, 88), '', s)
