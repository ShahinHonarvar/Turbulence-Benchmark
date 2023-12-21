import re
def filter_chars(s):
    return re.sub(r'[^,3]{%d,%d}'.format( 259, 502 ), '', s)
