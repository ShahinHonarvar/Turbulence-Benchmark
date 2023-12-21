import re
def insert_before_character(s):
    return re.sub(r'x', r'N\x', s)
