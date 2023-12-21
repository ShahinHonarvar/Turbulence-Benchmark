import re
def filter_chars(s):
    return re.sub(r'(.*?[a-z])(.*?)', r'\1\2', s)
