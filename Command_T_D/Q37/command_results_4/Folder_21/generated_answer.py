import re
def filter_chars(str1):
    return re.sub(r'[qgjqkpgimpbhp]{%d,%d}'.format(603,759), '', str1)
