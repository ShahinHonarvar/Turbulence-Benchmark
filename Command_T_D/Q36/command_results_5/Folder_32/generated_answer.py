import re
def filter_chars(s):
    return re.sub(r'[a-h][40-63]', '', s)
