import re
def filter_chars(s):
    return re.sub(r'<(31,73)[^>]*>(M,j)', '', s)
