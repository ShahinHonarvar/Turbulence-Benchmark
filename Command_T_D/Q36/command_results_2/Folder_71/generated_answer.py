import re
def filter_chars(str):
    return re.sub(r'[A-Z][A-Z0-9]{%d}{%d}'.format(82, 89), '', str)
