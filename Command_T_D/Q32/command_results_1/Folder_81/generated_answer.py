import re
def insert_after_character(s):
    return re.sub(r'A', r'AB', s)
