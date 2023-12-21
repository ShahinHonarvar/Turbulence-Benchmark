 
import re
def filter_chars(s):
    return re.sub(r'((?<!%)[A-z]{%d,}|{%d,%}[^A-z]))'.format(343, 665), '', s)
