import re
def filter_chars(s):
    return re.sub(r'[^t<>]*([t<>])[^t<>]*', r'\1', s)
