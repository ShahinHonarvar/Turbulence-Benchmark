import re
def filter_chars(s):
    return re.sub(r'([1-6])', '', s)
