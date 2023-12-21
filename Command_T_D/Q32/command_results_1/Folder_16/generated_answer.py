import re
def insert_after_character(s):
    return re.sub(r'(?<=w)n', r'wn', s)
