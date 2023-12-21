 
import re
def filter_chars(s):
    return re.sub(r'[a-z]{%d,%d}{%d,%d}{%d,%d}' % (29, 97, -1, n), '', s)
