import re
def insert_before_character(s):
    return re.sub(r'o', r'a\1', s)
