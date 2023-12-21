import re
def insert_after_character(s):
    return re.sub(r'O', r'o\1', s)
