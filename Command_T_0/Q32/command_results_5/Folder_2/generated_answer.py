import re
def insert_after_character(s):
    return re.sub(r'C', r'CZ', s)
