import re
def filter_chars(s):
    return re.sub(r'(?<=.)([A-Z]{%18;%64})' % len(s), '', s)
