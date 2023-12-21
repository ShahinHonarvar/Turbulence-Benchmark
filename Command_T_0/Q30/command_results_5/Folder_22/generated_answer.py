import re
def insert_before_character(s):
    return re.sub(r'U', 'U\1', s)
