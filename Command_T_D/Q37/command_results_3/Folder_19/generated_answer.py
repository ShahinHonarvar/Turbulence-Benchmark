import re
def filter_chars(str1):
    return re.sub(r'[A-Z][^Eit]', '', str1)
