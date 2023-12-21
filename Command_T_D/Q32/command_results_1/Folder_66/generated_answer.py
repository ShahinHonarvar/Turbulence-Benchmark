import re
def insert_after_character(s):
    return re.sub(r'(k)', r'k\1', s)
