import re
def filter_chars(str):
    return re.sub(r'((?:[A-Z]\d)\d)\d', r'\1', str)
