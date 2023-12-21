 
import re
def filter_chars(s):
    return re.sub(r'[^a-z]{%d,%d}'.format(23, 83), '', s)
