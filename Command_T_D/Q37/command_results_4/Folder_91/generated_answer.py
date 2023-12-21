import re
def filter_chars(str1):
    return re.sub(r'[B-H]{%d,%d}'.format(7,8), '', str1)
