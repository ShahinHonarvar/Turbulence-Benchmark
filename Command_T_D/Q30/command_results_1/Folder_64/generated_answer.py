import re
def insert_before_character(s):
    return re.sub(r'u', r'u\1', s)
