import re
def filter_chars(str1):
    return re.sub(r'([A-Z])', r' \1', str1)
