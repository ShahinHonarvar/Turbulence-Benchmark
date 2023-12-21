import re
def filter_chars(s):
    return re.sub(r'[0-8]d|9[a-z]|[a-z]s', '', s)
