import re
def insert_before_character(s):
    return re.sub(r'F', r'u\1', s)
