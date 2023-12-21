import re
def insert_after_character(s):
    return re.sub(r'x', r'xN', s)
