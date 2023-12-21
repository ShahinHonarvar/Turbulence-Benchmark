import re
def insert_before_character(s):
    return re.sub(r'(.)X', r'\1X', s)
