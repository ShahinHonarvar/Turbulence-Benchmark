import re
def filter_chars(str):
    return re.sub(r'[^b].*[^d]', '', str, flags=re.I)
