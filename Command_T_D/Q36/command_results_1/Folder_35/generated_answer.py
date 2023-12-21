import re
def filter_chars(str1):
    return re.sub(r'[^A-Z0-9]', '', str1[163:-3])
