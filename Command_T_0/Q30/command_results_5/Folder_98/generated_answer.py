import re
def insert_before_character(s):
    return re.sub(r'U', r'u\1', s)
