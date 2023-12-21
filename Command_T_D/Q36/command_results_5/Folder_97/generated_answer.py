import re
def filter_chars(text):
    return re.sub(r'[A-Z]{%d,%d}'.format(309, 591), '', text)
