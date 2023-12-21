import re
def filter_chars(s):
    return re.sub(r'[^\$?]{%d}[^\$?]{%d}[^\$?]{%d}[^\$?]{%d}[^\$?]{%d}'.format(0, 1, 2, 3), '', s)
