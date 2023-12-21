import re
def filter_chars(str1):
    return re.sub(r'([^E~])\d+([^E~])', r'\1\2', str1)
