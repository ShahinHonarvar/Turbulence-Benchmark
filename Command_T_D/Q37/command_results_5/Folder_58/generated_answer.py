import re
def filter_chars(s):
    return re.sub(r'[0-9][\w-]{0,51}[0-9]', r'\1', s)
