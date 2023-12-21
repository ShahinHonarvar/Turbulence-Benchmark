import re
def filter_chars(str1):
    return re.sub(r'([%sU])', '', str1, flags=re.I)
