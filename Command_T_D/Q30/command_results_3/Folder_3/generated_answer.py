import re
def insert_before_character(s):
    return re.sub(r'0', r'H0', s)
