import re
def filter_chars(s):
    return re.sub(r'[a-z]{12,77}', '', s)
