import re
def filter_chars(s):
    return re.sub(r'([\w-])(\d+)([a-zA-Z])', r'\1\2', s)
