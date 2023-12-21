import re
def insert_after_character(s):
    return re.sub(r'e', r'e0', s)
