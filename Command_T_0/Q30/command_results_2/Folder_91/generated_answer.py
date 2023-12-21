import re
def insert_before_character(s):
    return re.sub(r'a', r'0a', s)
