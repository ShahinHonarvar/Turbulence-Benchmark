import re
def filter_chars(s):
    return re.sub(r'[a-z]', '', s[55:-1])
