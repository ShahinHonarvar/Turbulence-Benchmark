import re
def filter_chars(s):
    return re.sub(r'[A-Z][a-z]{%d}{%d}'.format(ord('a') - 1, ord('q') - 1), '', s)
