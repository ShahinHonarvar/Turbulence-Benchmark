 
import re
def filter_chars(s):
    return re.sub(r'[a-i]{%d,%d}'.format(36,79), '', s)
