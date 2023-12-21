import re
def insert_before_character(s):
    return re.sub(r'0', 'H0', s)
