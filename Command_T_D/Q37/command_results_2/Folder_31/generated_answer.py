import re
def filter_chars(s):
    return re.sub(r'<(.)(w)+', r'\1', s)
