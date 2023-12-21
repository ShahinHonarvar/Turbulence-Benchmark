import re
def filter_chars(s):
    return re.sub(r'[tT][^xX]*[xX]', '', s)
