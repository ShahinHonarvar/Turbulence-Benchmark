import re
def filter_chars(s):
    return re.sub(r'(8[0-9][a-e])', '', s)
