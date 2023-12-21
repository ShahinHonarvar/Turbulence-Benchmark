import re
def filter_chars(s):
    return re.sub(r'([^f^o]\\d|g|i|j|k|l|m|n|o)','_',s)
