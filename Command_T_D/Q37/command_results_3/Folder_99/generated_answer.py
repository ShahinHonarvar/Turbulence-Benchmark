import re
def filter_chars(s):
    return re.sub(r'[^Th]{%d,%d}'.format(373, 901), '', s)
