import re
def filter_chars(str1):
    str1 = re.sub(r'([A-Z])', r' \1', str1)
    str1 = re.sub(r'([a-z])([A-Z])', r'\1 \2', str1)
    return str1
