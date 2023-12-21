import re
def filter_chars(string):
    return re.sub(r'[^aZbc]{%d,%d}'.format(41, 56), '', string)
