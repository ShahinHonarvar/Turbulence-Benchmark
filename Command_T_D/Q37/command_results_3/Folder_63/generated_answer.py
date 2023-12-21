 
import re
def filter_chars(s):
    return re.sub(r'(?i)[/a]{%d,%d}'.format(42, 92), '', s)
