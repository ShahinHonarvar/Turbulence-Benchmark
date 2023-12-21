import re
def filter_chars(s):
    return re.sub(r'[^%U]{%d,%d}'.format( 343, 665 ), '', s)
