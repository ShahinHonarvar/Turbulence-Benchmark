import re
def insert_before_character(s):
    return re.sub(r'c', 'cG', s)
