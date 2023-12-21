import re
def insert_after_character(s):
    return re.sub(r'a', r'0\1', s)
