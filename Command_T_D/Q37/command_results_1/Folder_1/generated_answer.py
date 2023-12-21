import re
def filter_chars(text):
    return re.sub(r'[A-Z]{%d,%d}' % (41, 79), '', text)
