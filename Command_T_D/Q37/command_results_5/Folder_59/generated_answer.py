import re
def filter_chars(s):
    return re.sub(r'([a-zA-Z])[2-3]', r'\1', s)
