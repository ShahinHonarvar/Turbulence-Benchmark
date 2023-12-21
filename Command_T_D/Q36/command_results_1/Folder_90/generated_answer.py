import re
def filter_chars(str):
    return re.sub(r'[^\d~f]', '', str, flags=re.I)
