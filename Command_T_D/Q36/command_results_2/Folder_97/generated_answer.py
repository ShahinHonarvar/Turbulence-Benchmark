import re
def filter_chars(string):
    return re.sub(r'[A-Z][^A-Z]*[A-Z]', r'', string)
