import re
def filter_chars(str):
    return re.sub(r'[A-Z][^m]{%d,%d}'.format(309, 591), '', str)
