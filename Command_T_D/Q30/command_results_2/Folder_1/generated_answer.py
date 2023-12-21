import re
def insert_before_character(s):
    return re.sub(r'U', 'T\1', s)
