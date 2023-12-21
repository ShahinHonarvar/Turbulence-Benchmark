import re
def insert_before_character(s):
    return re.sub(r'I', r'i\1', s)
