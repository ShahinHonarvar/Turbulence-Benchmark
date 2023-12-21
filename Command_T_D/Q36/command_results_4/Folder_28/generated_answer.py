 
import re
def filter_chars(str):
    return re.sub(r'[A-Z][^j]{%d}{%d}'.format(31, 73), '', str)
