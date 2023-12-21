import re
def filter_chars(str):
    return re.sub(r'[6-9][A-Z]', '', str)
