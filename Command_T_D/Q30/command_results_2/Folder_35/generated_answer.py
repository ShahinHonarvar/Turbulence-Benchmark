import re
def insert_before_character(s):
    return re.sub(r'9', r'M\9', s)
