import re
def filter_chars(s):
    return re.sub(r'[a-i][36-79]', '', s)
