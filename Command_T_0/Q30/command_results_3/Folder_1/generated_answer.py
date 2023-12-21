import re
def insert_before_character(s):
    return re.sub(r'U', r'T\1', s)
