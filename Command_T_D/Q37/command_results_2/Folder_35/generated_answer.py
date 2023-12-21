import re
def filter_chars(s):
    return re.sub(r'[^A-Z0-9]([A-Z0-9][^A-Z0-9]*)', '', s)
