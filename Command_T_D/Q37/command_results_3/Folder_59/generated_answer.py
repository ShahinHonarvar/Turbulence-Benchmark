import re
def filter_chars(str):
    return re.sub(r'[5-9][^5-9]_[^5-9]', '', str)
