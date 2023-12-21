import re
def insert_after_character(s):
    return re.sub(r'(.)X', r'\1X', s)
