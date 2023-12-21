import re
def insert_before_character(s):
    return re.sub(r't', r'u\1', s)
