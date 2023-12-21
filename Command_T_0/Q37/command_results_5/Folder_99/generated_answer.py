import re
def filter_chars(s):
    return re.sub(r'[Tg][^h]{%d,%d}'.format(373,901), '', s)
