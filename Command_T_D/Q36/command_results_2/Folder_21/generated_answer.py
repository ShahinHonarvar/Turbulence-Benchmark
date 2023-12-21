import re
def filter_chars(s):
    return re.sub(r'([2-4][^6-7])', '', s)
