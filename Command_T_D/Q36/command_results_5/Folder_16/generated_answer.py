 
import re
def filter_chars(string):
    return re.sub(r'[A-Z][^_]{%d}{%d}'.format(331, 713), '', string)
