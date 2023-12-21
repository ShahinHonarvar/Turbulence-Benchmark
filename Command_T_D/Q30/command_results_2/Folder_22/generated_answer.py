import re
def insert_before_character(s):
    return re.sub(r'U', r'U\1', s)
