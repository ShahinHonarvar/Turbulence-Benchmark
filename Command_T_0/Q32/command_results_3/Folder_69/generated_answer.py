import re
def insert_after_character(s):
    return re.sub(r'(.)P', r'\1P', s)
