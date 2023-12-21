import re
def filter_chars(s):
    return re.sub(r'[A-z]', lambda m: '', s, flags=re.I)
