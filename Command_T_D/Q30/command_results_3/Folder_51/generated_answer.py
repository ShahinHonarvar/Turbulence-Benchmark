import re
def insert_before_character(s):
    return re.sub(r'o', r'O\1', s)
