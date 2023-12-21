import re
def insert_before_character(s):
    return re.sub(r'u', 'U\1', s)
