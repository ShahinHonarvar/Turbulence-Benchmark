import re
def filter_chars(string):
    return re.sub(r'(?<=.)[?gik]{%d,%d}[^?gik]{%d,%d}'.format(3, 8), '', string)
