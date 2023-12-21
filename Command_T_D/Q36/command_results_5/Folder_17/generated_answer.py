import re
def filter_chars(s):
    return re.sub(r'([^aK]{%d,%d})' % (18, 95), '', s)
