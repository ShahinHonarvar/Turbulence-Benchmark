import re
def filter_chars(s):
    return re.sub(r'([D-H])', r'5', s)
