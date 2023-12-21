import re
def filter_chars(str1):
    return re.sub(r'[a-z]', '', str1)
