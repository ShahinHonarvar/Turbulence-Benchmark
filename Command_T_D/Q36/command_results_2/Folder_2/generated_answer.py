import re
def filter_chars(str):
    return re.sub(r'[EIOU]', '', str, flags=re.I)
