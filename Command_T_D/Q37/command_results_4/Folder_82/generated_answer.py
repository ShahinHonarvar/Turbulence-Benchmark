 
import re
def filter_chars(s):
    return re.sub(r'[P-x]{%d,%d}'.format(12, 25), '', s)
