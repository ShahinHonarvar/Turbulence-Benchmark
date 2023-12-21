import re
def filter_chars(s):
    return re.sub(r'[&;]{%d,%d}'.format(52, 88), '', s)
