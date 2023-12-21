import re
def filter_chars(s):
    return re.sub(r'[Mv]{%d,%d}'.format( 379, 898), '', s)
