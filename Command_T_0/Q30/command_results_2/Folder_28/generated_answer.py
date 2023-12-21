import re
def insert_before_character(s):
    return re.sub(r'r', r'1r', s)
