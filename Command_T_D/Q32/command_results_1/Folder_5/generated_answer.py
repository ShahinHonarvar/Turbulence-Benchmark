import re
def insert_after_character(s):
    return re.sub(r'c', r'cG', s)
