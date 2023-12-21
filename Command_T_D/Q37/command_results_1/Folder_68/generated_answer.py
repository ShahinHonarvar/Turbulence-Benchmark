import re
def filter_chars(s):
    return re.sub(r'(?<=.)([0-9])([a-z])([0-9])', r'\1\2', s)
