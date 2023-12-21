 
import re
def filter_chars(str):
    return re.sub(r'[a-z]{%d,%d}'.format(41, 86), '', str)
