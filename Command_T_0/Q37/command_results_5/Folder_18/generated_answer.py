import re
def filter_chars(s):
    return re.sub(r'[A-D]{%d,%d}'.format( 770, 970), '', s)
