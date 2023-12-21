import re
def filter_chars(s):
    return re.sub(r'[A-Za-z]+', '', s[56:-86])
