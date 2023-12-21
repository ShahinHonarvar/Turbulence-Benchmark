import re
def filter_chars(str):
    return re.sub(r'[A-Z][/][0-5]', '', str)
