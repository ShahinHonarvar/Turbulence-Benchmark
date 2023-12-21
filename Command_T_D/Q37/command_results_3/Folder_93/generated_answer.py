import re
def filter_chars(str):
    return re.sub(r'[H-e]', '', str)
