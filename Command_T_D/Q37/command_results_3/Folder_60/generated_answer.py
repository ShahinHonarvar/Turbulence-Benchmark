import re
def filter_chars(s):
    return re.sub(r'(.)\d{4}(L)', r'\1', s)
