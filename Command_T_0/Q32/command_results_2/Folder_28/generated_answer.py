import re
def insert_after_character(s):
    return re.sub(r'r', r'1\1', s)
