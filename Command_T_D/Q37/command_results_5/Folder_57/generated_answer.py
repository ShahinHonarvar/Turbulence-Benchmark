import re
def filter_chars(text):
    return re.sub(r'[A-Z][\d]{%d,%d}'.format(27,85), '', text)
