import re
def filter_chars(s):
    return re.sub(r'[tT][^v]v', '', s)
