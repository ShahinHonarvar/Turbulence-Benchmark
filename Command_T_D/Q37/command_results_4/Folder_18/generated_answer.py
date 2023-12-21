import re
def filter_chars(str):
    return re.sub(r'\A-D', '', str[770:-30], flags=re.I)
