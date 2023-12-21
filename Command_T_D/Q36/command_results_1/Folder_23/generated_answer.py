import re
def filter_chars(s):
    return re.sub(r'(?<=\d)[\d]5', '', s)
