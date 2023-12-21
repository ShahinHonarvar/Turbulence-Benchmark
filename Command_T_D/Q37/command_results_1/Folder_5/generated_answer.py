import re
def filter_chars(s):
    return re.sub(r'<[5-]=82', '', s)
